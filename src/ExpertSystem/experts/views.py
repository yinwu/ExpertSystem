from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render
from experts.models import *
from django.contrib import auth

from .forms import ExpertForm

def login(request):
    return render(request, 'login.html')

def login_validation(request):
    next_url = request.GET.get("next")
    username = request.POST.get("name")
    passwd = request.POST.get("passwd")

    print(username)
    print(passwd)

    user_obj = auth.authenticate(request, username=username, password=pwd)
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

def expert_list(request):
    expert_list = Expert.objects.filter(visible=True)
    return render(request, 'expert_list_template.html', {"result":expert_list})

@login_required
def delete_expert_req(request, expert_id):

    expert_to_delete = Expert.objects.get(id=expert_id)
    expert_to_delete.visible = False
    expert_to_delete.save()
    return redirect("/experts/list") 

@login_required
def add_expert_req(request):
    if request.method == 'GET':
        return render(request, 'add_expert_template.html')
        
    if request.method == 'POST':
        form = ExpertForm(request.POST)
        new_expert_name = request.POST["name"]
        if form.is_valid():
            form.save()
            new_expert = Expert.objects.get(name=new_expert_name)
            return redirect("/experts/detail/"+str(new_expert.id))
        else:
            return HttpResponse("添加专家信息失败")
    else:
        return redirect("program/list")
        

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
            form.save()
            return redirect("/experts/detail/"+ str(expert_id))
        else:
            return HttpResponse("修改专家信息失败")
        
        return redirect("/experts/list")
        
def search(request):
    test_data = [
        {"id":"1", "name":"name1", "responser":"responser1", "description":"descriptino1", "info":"info1"},
        {"id":"2", "name":"name2", "responser":"responser2", "description":"descriptino2", "info":"info2"},
        {"id":"3", "name":"name3", "responser":"responser3", "description":"descriptino3", "info":"info3"},
        {"id":"4", "name":"name4", "responser":"responser4", "description":"descriptino4", "info":"info4"},
        {"id":"5", "name":"name5", "responser":"responser5", "description":"descriptino5", "info":"info5"},
        {"id":"6", "name":"name6", "responser":"responser6", "description":"descriptino6", "info":"info6"},
        {"id":"7", "name":"name7", "responser":"responser7", "description":"descriptino7", "info":"info7"},
        {"id":"8", "name":"name8", "responser":"responser8", "description":"descriptino8", "info":"info8"},
        {"id":"9", "name":"name9", "responser":"responser9", "description":"descriptino9", "info":"info9"},
        {"id":"10", "name":"name10", "responser":"responser10", "description":"descriptino10", "info":"info10"}
    ]
    keyStr = request.GET.get('search_str')
    print(keyStr)
   
    expert_list = Expert.objects.filter(name = keyStr)
    return render(request, 'expert_list_template.html', {"result":expert_list})
    
   
def comments(request, expert_id, program_id):
    expert = Expert.objects.get(id=expert_id)
    program = Program.objects.get(id=program_id)
    example_comments = {"expert_id": expert_id, "program_id":program_id, "score":"100", "comment_date":"2020-01-01", "comments":"评审通过"}
    return render(request, 'expert_program_comments.html', {"expert" : expert, "program": program, "comment" : example_comments})  
       
def save_comments(request, expert_id, program_id):
    score = request.GET.get('score')
    comment_date = request.GET.get('comment_date')
    comments = request.GET.get('remarks')
    return redirect("/experts/detail/" + str(expert_id))
              
      
