import os
import random
from django.shortcuts import render, redirect


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
from program.models import Program

from django.forms.models import model_to_dict

def program_list(request):
    program_list = Program.objects.filter(visible=True)
    return render(request, 'program_list_template.html', {"program_list": program_list})

def program_detail(request, program_id):
    try:
        program_detail_info = Program.objects.get(id=program_id)
    except:
        return HttpResponse("项目不存在， ID:", program_id)
    
    comment_list = Comments.objects.filter(program__id = program_id).exclude(status="nok")
    # expert_dict = {}
    # for item in expert_list:
    #     comment = Comments.objects.filter(expert__id=item.id).filter(program__id=program_id)[0]
    #     item = model_to_dict(item)
    #     item["status"] = comment.status
    #     expert_dict.append(item)
        
    # print(expert_dict)

    return render(request, 'program_detail.html', {"expert_list" : comment_list, "program": program_detail_info})

def program_check(request):
    return render(request, 'program_check_template.html')

def program_check(request):
    return render(request, 'program_check_template.html')

@login_required()
def program_select_experts(request, id):
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
                new_comment.save()

        return redirect('/program/detail/'+str(program.id))
    
def expert_exclude(request, expert_id, program_id):
    comments = Comments.objects.filter(expert__id = expert_id, program__id = program_id)
    if comments.count() > 0:
        comment = comments[0]
        comment.status = "nok"
        comment.save()
        return redirect("/program/detail/"+str(program_id))
    else:
        return HttpResponse("确认专家失败")

    return redirect("/program/detail/" + str(program_id))


def program_export_experts(request, id):
    return render(request, 'export_expert_template.html')


def program_add(request):
    
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
    
def program_delete(request, id):    
    # Program.objects.get(id=id).delete()
    program_to_delete = Program.objects.get(id=id)
    program_to_delete.visible = False
    program_to_delete.save()
    return redirect("/program/list") 

def save_program(request):
    if request.method == "POST":
        program_form = ProgramForm(request.POST)
        print(request.POST)
        if  program_form.is_valid():
            program_form.save()
            print("New program saved succefully")
        else:
            print("New program save failed")
            return HttpResponse("添加新项目失败")

    return redirect("/program/list")
            
   
def search(request):
    
    keyStr = request.GET.get('name')
    post_list = Program.objects.filter(name = keyStr)
    return render(request, 'program_list_template.html', {"program_list": post_list})
    
     
    
def program_modify(request, id):
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
        
def download_table(request, id):
    print("enter download table")
    file_name = 'expertfile/test_' + str(id) + '.xlsx'
    file_path = os.path.join(os.getcwd(), file_name)
    print(file_path)
    if os.path.exists(file_path):
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="mytest.xlsx"'
        print("file exist")
        return response

    else:
        print("raise 404")
        raise Http404

def expert_confirm(request, program_id, expert_id):
    
    comments = Comments.objects.filter(expert__id = expert_id, program__id = program_id)
    if comments.count() > 0:
        comment = comments[0]
        comment.status = "ok"
        comment.save()
        return redirect("/program/detail/"+str(program_id))
    else:
        return HttpResponse("确认专家失败")