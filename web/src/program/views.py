import os
import random
import xlwt
import xlrd
from xlrd import xldate_as_tuple, xldate_as_datetime
from datetime import timezone, datetime
from dateutil import tz, zoneinfo
from django.utils.http import urlquote
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.http import FileResponse

from django.shortcuts import render
from django.db.models import Q


from experts.models import Expert, Comments
from program.models import Program
from program.forms import ProgramForm

from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist


def program_list(request):
    # 领导和管理员可以进行看到所有项目
    if request.user.username == "admin":
        program_list = Program.objects.filter(visible=True)
        return render(request, 'program_list_template.html', {"program_list": program_list})
    else:
        # 只展示跟自己有关系的项目：
        user_name = request.user.username
        try:
            request_expert = Expert.objects.get(account__username = user_name)
        except ObjectDoesNotExist:
            return redirect("/experts/login/")
        else:
            comments = Comments.objects.filter(expert = request_expert)
            program_list = Program.objects.filter(selected = request_expert)

            return render(request, 'program_list_template.html', {"program_list": program_list}) 


def program_detail(request, program_id):
    try:
        program_detail_info = Program.objects.get(id=program_id)
    except:
        return HttpResponse("项目不存在， ID:", program_id)
    
    comment_list = Comments.objects.filter(program__id = program_id).exclude(status="nok")
    return render(request, 'program_detail.html', {"expert_list" : comment_list, "program": program_detail_info})

def program_check(request):
    return render(request, 'program_check_template.html')

def program_check(request):
    return render(request, 'program_check_template.html')

@login_required()
def program_select_experts(request, id):
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限抽取专家")

    program = Program.objects.get(id=id)

    if request.method == 'GET':
        return render(request, 'select_expert_template.html', {"program": program})
    if request.method == 'POST':
        level_value = request.POST.get('level')
        degree_value = request.POST.get('degree')
        program_type_value = request.POST.get('program_type')
        request_experts_count = int(request.POST.get('number'))

        # 合并用户的过滤条件
        q = Q()
        q.connector = "AND"
        if level_value != "all":
            q.children.append(("level",level_value))
        if degree_value != "all":
            q.children.append(("degree",degree_value))
        if program_type_value != "all":
            q.children.append(("program_type",program_type_value))

        # 已确认专家数量（不管专家是否符合新条件，只要确认过就予以保留）
        confirmed_experts = Comments.objects.filter(program__id = id).filter(status="ok")
        
        # 要删除的专家数量
        count_to_selected = request_experts_count - confirmed_experts.count()

        # 请求抽取的专家数量 小于 已确认的专家数量
        if count_to_selected < 0:
            # 删除的夺取的专家
            experts_to_delete = random.sample(list(confirmed_experts), (0-count_to_selected))
            for expert in experts_to_delete:
                expert.delete()
        
        # 要抽取的专家数量大于已确认专家的数量，不做任何处理
        elif count_to_selected >= 0:
            # 解绑抽取后未确认的专家
            expert_wait_for_confirm = Comments.objects.filter(program__id = id).filter(status="unknow")
            for item in expert_wait_for_confirm:
                item.delete()
            
            # 未确认的专家已经跟项目解绑，selected_program_list__id=id 只剩下已排除和已确认的
            available_experts = Expert.objects.filter(q).exclude(
                selected_program_list__id=id).exclude(visible=False)
            selected_expert_list = {}

            # 备选的专家数小于要求
            if count_to_selected > available_experts.count():
                return HttpResponse("没有足够的专家供您抽取，请您添加专家，修改限制条件，或者减少本次抽签专家数量")
        
            # 从候选队列中抽取专家数量
            selected_expert_list = random.sample(list(available_experts), count_to_selected)

            for item in selected_expert_list:
                new_comment = Comments()
                new_comment.expert = item
                new_comment.program = program
                new_comment.valuation_status = "unvaluated"
                new_comment.save()
                print("have created comment item!!!")

        return redirect('/program/detail/'+str(program.id))

@login_required
def expert_exclude(request, expert_id, program_id):

    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限添加项目")

    comments = Comments.objects.filter(expert__id = expert_id, program__id = program_id)
    if comments.count() > 0:
        comment = comments[0]
        comment.status = "nok"
        comment.save()
        return redirect("/program/detail/"+str(program_id))
    else:
        return HttpResponse("确认专家失败")

    return redirect("/program/detail/" + str(program_id))

def buildFile(program_id):
    if Comments.objects.filter(program__id = program_id).exclude(status="nok").exists():
        
        return True
    else:
        return False
    
    

def program_export_experts(request, id):
    program = Program.objects.get(id=id)
    allow_export = Comments.objects.filter(program__id = id).exclude(status="nok").exists()
    if request.method == 'GET':
        return render(request, 'export_expert_template.html', {"program": program, "allow_export":allow_export})
    if request.method == 'POST':
        filename = request.POST.get('fileName')
        program = Program.objects.get(id=id)
        if len(filename) == 0:
            tz_bj = tz.gettz('Asia/Beijing')
            date_time = datetime.now(tz=tz_bj)
            file_name = "{}-{}.xls".format(program.name, date_time.strftime("%Y%m%d"))    
        else:
            file_name = filename + ".xls"
        return download_table(request, id, file_name)
        

@login_required
def program_add(request):
    
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限添加专家")

    if request.method == 'GET':
        return render(request, 'add_program_template.html')
    
    if request.method == 'POST':
        new_program = ProgramForm()
        program_responser = request.POST.get('responser')
        program_seq = request.POST.get('code')
        program_name = request.POST.get('name')
        program_location = request.POST.get('location')
        program_money = request.POST.get('budget')
        program_description = request.POST.get('remarks')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        program_date = request.POST.get('program_date')
        remarks = request.POST.get('remarks')
        new_program = Program(name= program_name,seq=program_seq,responser=program_responser,location=program_location,money=program_money,start_date=start_date,end_date=end_date,program_date=program_date,desp=remarks)
        new_program.save()
        
        return redirect("/program/list") 
    
@login_required
def program_delete(request, id):

    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限删除项目")

    # Program.objects.get(id=id).delete()
    program_to_delete = Program.objects.get(id=id)
    program_to_delete.visible = False
    program_to_delete.save()
    return redirect("/program/list") 

@login_required
def save_program(request):
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限添加项目")

    if request.method == "POST":
        program_form = ProgramForm(request.POST)
        print(request.POST)
        if  program_form.is_valid():
            program_form.save()
        else:
            return HttpResponse("添加新项目失败")

    return redirect("/program/list")
            
@login_required  
def search(request):
    keyStr = request.GET.get('name')
    if request.user.username == "admin":
        program_list = Program.objects.filter(visible=True)
    else:
        user_name = request.user.username
        try:
            request_expert = Expert.objects.get(account__username = user_name)
        except ObjectDoesNotExist:
            return redirect("/experts/login/")
        else:
            comments = Comments.objects.filter(expert = request_expert)
            program_list = Program.objects.filter(selected = request_expert)
    post_list = program_list & (Program.objects.filter(name__contains=keyStr).all() | Program.objects.filter(responser__contains=keyStr).all() |\
    Program.objects.filter(location__contains=keyStr).all() | Program.objects.filter(seq__contains=keyStr).all() |\
    Program.objects.filter(money__contains=keyStr).all() | Program.objects.filter(desp__contains=keyStr).all() |\
    Program.objects.filter(program_date__contains=keyStr).all() | Program.objects.filter(start_date__contains=keyStr).all() |\
    Program.objects.filter(end_date__contains=keyStr).all())
    
    return render(request, 'program_list_template.html', {"program_list": post_list})
    

def program_modify(request, id):
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限修改该项目")

    if request.method == 'GET':
        program = Program.objects.get(id=id)
        return render(request, 'modify_program_template.html', {"program_item": program, "program_id": id})
    
    if request.method == 'POST':
        program_name = request.POST.get('name')
        program_responser = request.POST.get('responser')
        program_seq = request.POST.get('code')
        program_money = request.POST.get('budget')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        program_date = request.POST.get('program_date')
        location = request.POST.get('location')
        remarks = request.POST.get('remarks')
        modify_program = Program.objects.get(id=id)
        modify_program.name = program_name
        modify_program.responser = program_responser
        modify_program.seq = program_seq
        modify_program.start_date = start_date
        modify_program.end_date = end_date
        modify_program.program_date = program_date
        modify_program.location = location
        modify_program.desp = remarks
        modify_program.money = program_money
        modify_program.save()

        return redirect("/program/list")

@login_required
def download_table(request, id, file):
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限进行该操作") 
        
    program = Program.objects.get(id=id)
   
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;filename="%s"' % (urlquote(file))
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(program.name)
    
    # Creating style for file
    head_style = xlwt.XFStyle()
    head_style.font.bold = True
    body_style = xlwt.XFStyle()
    pattern_light = xlwt.Pattern()
    pattern_light.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern_light.pattern_fore_colour = 22
    pattern_white = xlwt.Pattern()
    pattern_white.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern_white.pattern_fore_colour = 1
    
    # Sheet header, first row
    row_num = 0
    columns = ['专家姓名', '职务等级', '工作单位', '联系电话', '最高学历', '专业类型', '确认状态', '评审意见']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], head_style)
        
    # Sheet body, remaining rows
    comments = Comments.objects.filter(program__id = id).exclude(status="nok")
    for comment in comments:
        row_num += 1
        if row_num % 2 == 0:
            body_style.pattern = pattern_light
        else:
            body_style.pattern = pattern_white       
        expert = comment.expert
        ws.write(row_num,0, expert.name, body_style)
        ws.write(row_num,1, expert.level, body_style)
        ws.write(row_num,2, expert.unit, body_style)
        ws.write(row_num,3, expert.phone, body_style)
        ws.write(row_num,4, expert.degree, body_style)
        ws.write(row_num,5, expert.program_type, body_style)
        if comment.status == 'ok':
            ws.write(row_num,6, '已确认', body_style)
        else:
            ws.write(row_num,6, '待确认', body_style)
        if comment.valuation_status == 'pass':
            ws.write(row_num,7, '评审通过', body_style)
        else:
            if comment.valuation_status == 'nopass':
                ws.write(row_num,7, '评审不通过', body_style)
            else:
                ws.write(row_num,7, '待评审', body_style)
                    
    wb.save(response)
    return response

def expert_confirm(request, program_id, expert_id):
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限进行该操作") 

    comments = Comments.objects.filter(expert__id = expert_id, program__id = program_id)
    if comments.count() > 0:
        comment = comments[0]
        comment.status = "ok"
        comment.save()
        return redirect("/program/detail/"+str(program_id))
    else:
        return HttpResponse("确认专家失败")

@login_required       
def program_import(request):
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限进行该操作")
        
    if request.method == 'GET':
        return render(request, 'import_program_template.html')
    else:
        if request.method == 'POST':
            f = request.FILES.get("uploadFile") 
            excel_type = f.name.split('.')[1]
            
            if excel_type in ['xlsx','xls']:
                # 开始解析上传的excel表格
                wb = xlrd.open_workbook(filename=None,file_contents=f.read())
                table = wb.sheets()[0]
                rows = table.nrows  # 总行数
                
                for i in range(1,rows):
                    rowVlaues = table.row_values(i)
                    #strftime('%Y-%m-%d %H:%M:%S')
                    #date = (datetime(*xldate_as_tuple(rowVlaues[6],0))).
                    create_date = xldate_as_datetime(rowVlaues[6],0).strftime('%Y-%m-%d')
                    start_date = xldate_as_datetime(rowVlaues[7],0).strftime('%Y-%m-%d')
                    finish_date = xldate_as_datetime(rowVlaues[8],0).strftime('%Y-%m-%d')
                    
                    new_program = ProgramForm()
                    new_program = Program(seq=rowVlaues[0],name= rowVlaues[1],desp=rowVlaues[2], responser=rowVlaues[3],\
                    location=rowVlaues[4],money=rowVlaues[5],program_date=create_date,start_date=start_date,end_date=finish_date)
                    new_program.save() 
                program_list = Program.objects.filter(visible=True)                    
                return render(request,'program_list_template.html',{"program_list": program_list})
            else:
                return render(request,'import_program_template.html',{'message':'导入失败: 需导入.xlsx 或.xls excel格式文件'})
           