from django.shortcuts import render, redirect
import xlrd

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse
from django.shortcuts import render
from experts.models import *
from django.contrib import auth

from .forms import ExpertForm
from django.core.exceptions import ObjectDoesNotExist

def delete_user(expert):
    try:
        user_to_delete = User.objects.get(name=expert.phone)
        user_to_delete.delete()
    except:
        print("WARNING:该专家没有账户要删除")

def add_user(expert):
    new_expert_phone = expert.phone
    new_user = User()
    new_user.username = new_expert_phone
    new_user.password = new_expert_phone
    new_user.is_staff = True
    new_user.is_active = True
    new_user.save()
    user_group = Group.objects.get(id=2)
    new_user.groups.add(user_group)
    expert.account = new_user
    expert.save()
    print("用户创建成功")

def update_user(expert, new_name):
    try:
        user = User.objects.get(name = expert.phone)
        user.username = new_name
        user.save()
    except:
        print("更新用户账户信息失败")


def user_login(request):
    next_url = request.GET.get('next', '')
    print(next)
    if request.method == "POST":
        user_name = request.POST["user_name"]
        user_password = request.POST["user_password"]

        user = authenticate(username=user_name, password=user_password)
        if user:
            login(request, user)
            if next_url:
                print("next url:", next_url)
                return redirect(next_url)
            else:
                return redirect("/program/list")
        else:
            return HttpResponse("输入的用户名和密码错误")
    else:
        return render(request, 'login.html')

def login_out_user(request):
    logout(request)
    return redirect("/experts/login/")

def login_validation(request):
    next_url = request.GET.get("next")
    username = request.POST.get("name")
    passwd = request.POST.get("passwd")

    user_obj = auth.authenticate(request, username=username, password=passwd)
    if user_obj:
        # 用户名和密码正确
        auth.login(request, user_obj)  # 给该次请求设置了session数据，并在响应中回写cookie
        if next_url:
            return redirect(next_url)
        else:
            return redirect("/book_list/")
    else:
        # 用户名或密码错误
        return render(request, "login.html", {"error_msg": "用户名或密码错误"})

def index(request):
    return render(request, 'index.html')

@login_required
def expert_list(request):
    login_user = request.user.username
    if login_user == "admin":
        expert_list = Expert.objects.filter(visible=True)
        return render(request, 'expert_list_template.html', {"result":expert_list})
    else:
        try:
            request_expert = Expert.objects.get(phone = login_user)
        except:
            return redirect("/experts/login/")
        return redirect("/experts/detail/" + str(request_expert.id)) 


@login_required
def delete_expert_req(request, expert_id):
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限删除专家")

    expert_to_delete = Expert.objects.get(id=expert_id)
    expert_to_delete.visible = False
    expert_to_delete.save()

    # 删除该专家的账户
    delete_user(expert_to_delete)

    return redirect("/experts/list/") 

#暂时只检查电话号码长度,电话号码不能少于8位
def is_valid_phone_no(phone_number):
    return False if len(phone_number) < 8 else True

@login_required
def add_expert_req(request):
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限删除专家")

    if request.method == 'GET':
        return render(request, 'add_expert_template.html')
        
    if request.method == 'POST':
        form = ExpertForm(request.POST)
        new_expert_name = request.POST["name"]
        new_expert_phone = request.POST["phone"]

        if is_valid_phone_no(new_expert_phone) == False:
            return HttpResponse("电话号码格式不正确")

        #用电话号码，联系方式不能重复
        if Expert.objects.filter(phone=new_expert_phone).count() > 0:
            return HttpResponse("系统中已有该专家信息")

        if form.is_valid():
            form.save()
            new_expert = Expert.objects.get(name=new_expert_name)
            # 为该专家创建用户
            add_user(new_expert)

            return redirect("/experts/detail/"+str(new_expert.id))
        else:
            return HttpResponse("添加专家信息失败")
    else:
        return redirect("program/list")
        
@login_required
def expert_detail(request, expert_id):

    try:
        expert = Expert.objects.get(id = expert_id)
    except:
        return HttpResponse("专家不存在，ID:", expert_id)
    
    program_list = expert.selected_program_list.all()
    #return render(request, 'expert_detail.html', {"expert":expert})
    return render(request, 'expert_detail.html', {"expert" : expert, "program_list": program_list})

@login_required
def modify_expert_req(request, expert_id):
    """
    expert_form = ExpertForm()
    return render(request, 'add_expert_template.html', {"expert_form": expert_form})
    """
    if request.method == 'GET':
        try:
            expert = Expert.objects.get(id = expert_id)
        except:
            return HttpResponse("专家不存在，ID:", expert_id)
    
        program_list = expert.selected_program_list.all()
        return render(request, 'modify_expert_template.html', {"expert" : expert, "program_list": program_list})
    
    if request.method == 'POST':
        expert_to_modify = Expert.objects.get(id=expert_id)
        form = ExpertForm(request.POST,instance=expert_to_modify)
        if form.is_valid():
            if expert_to_modify.phone != request.POST["phone"]:
                update_user(expert_to_modify, request.POST["phone"])
            form.save()
            return redirect("/experts/detail/"+ str(expert_id))
        else:
            return HttpResponse("修改专家信息失败")
        
        return redirect("/experts/list/")

@login_required
def search(request):
    keyStr = request.GET.get('search_str')
    if request.user.username == "admin":
        expert_list = Expert.objects.filter(visible=True)
    else:
        return HttpResponse("您不是管理员，你没有权限搜索专家")
    
    return_list = expert_list & (Expert.objects.filter(name__contains=keyStr).all() | Expert.objects.filter(phone__contains=keyStr).all() |\
    Expert.objects.filter(email__contains=keyStr).all() | Expert.objects.filter(address__contains=keyStr).all() |\
    Expert.objects.filter(unit__contains=keyStr).all() | Expert.objects.filter(level__contains=keyStr).all() |\
    Expert.objects.filter(program_type__contains=keyStr).all() | Expert.objects.filter(degree__contains=keyStr).all())
   
    return render(request, 'expert_list_template.html', {"result":return_list})
    
@login_required
def comments(request, expert_id, program_id):
    expert = Expert.objects.get(id=expert_id)
    program = Program.objects.get(id=program_id)
    comment= Comments.objects.get(program=program, expert=expert)
    
    if request.method == 'GET':
        return render(request, 'expert_program_comments.html', {"expert" : expert, "program": program, "comment" : comment}) 
    if request.method == 'POST':
        comments = request.POST.get('remarks')    
        status = request.POST.get('valuationStatus')
        comment.content = comments
        comment.valuation_status = status
        comment.save()
        return redirect("/experts/detail/" + str(expert_id))

@login_required       
def import_experts(request):
    user = User.objects.get(username=request.user.username)
    if user.username != "admin":
        return HttpResponse("您不是管理员，你没有权限进行该操作")
        
    if request.method == 'GET':
        return render(request, 'import_expert_template.html')
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
                    new_expert_name = rowVlaues[0]
                    new_expert_phone = rowVlaues[1]

                    if is_valid_phone_no(str(new_expert_phone)) == False:
                        return HttpResponse("电话号码格式不正确")

                    existing_experts = Expert.objects.filter(phone=new_expert_phone)
                    for existing_expert in existing_experts:
                        if existing_expert.visible == True:
                            return HttpResponse("系统中有重复专家信息，请删除后再导入")
                    new_expert = Expert(name=rowVlaues[0], phone=str(int(rowVlaues[1])), email=rowVlaues[2], address=rowVlaues[3], unit=rowVlaues[4], degree=rowVlaues[5], program_type=rowVlaues[6], level=rowVlaues[7])
                    new_expert.save()
                    add_user(new_expert)
                    
                expert_list = Expert.objects.filter(visible=True)
                return render(request, 'expert_list_template.html', {"result":expert_list})
            else:
                return render(request,'import_expert_template.html',{'message':'导入失败: 需导入.xlsx 或.xls excel格式文件'})              
