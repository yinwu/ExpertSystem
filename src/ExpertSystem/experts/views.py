from django.shortcuts import render, redirect

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from experts.models import *


from .forms import ExpertForm

def index(request):
    return render(request, 'index.html')

def expert_list(request):
    expert_list = Expert.objects.all()
    return render(request, 'expert_list_template.html', {"result":expert_list})

    
def delete_expert_req(request, expert_id):
    expert_list = Expert.objects.all()
    return render(request, 'expert_list_template.html', {"result":expert_list})

def add_expert_req(request):
    """
    expert_form = ExpertForm()
    return render(request, 'add_expert_template.html', {"expert_form": expert_form})
    """
    if request.method == 'GET':
        return render(request, 'add_expert_template.html')
    
    if request.method == 'POST':
        print("POST")
        form = ExpertForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("添加专家信息失败")
        return redirect("/experts/list")

def expert_detail(request, expert_id):

    try:
        expert = Expert.objects.get(id = expert_id)
    except:
        return HttpResponse("专家不存在，ID:", expert_id)
    
    program_list = expert.selected_program_list.all()
    #return render(request, 'expert_detail.html', {"expert":expert})
    return render(request, 'expert_detail.html', {"expert" : expert, "program_list": program_list})


def save_expert_req(request):

    if request.method == "POST":
        print("POST")
        form = ExpertForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("添加专家信息失败")
    # TODO: 后期添加成功后 跳转到专家详情页面。
    return redirect("/experts/list")

   
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
        print("POST")
        form = ExpertForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
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
    
   
    
