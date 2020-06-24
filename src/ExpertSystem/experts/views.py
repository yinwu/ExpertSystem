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


def add_expert_req(request):
    expert_form = ExpertForm()
    return render(request, 'add_expert_template.html', {"expert_form": expert_form})

def expert_detail(request, expert_id):
    context = {"name":"test_name"}

    try:
        expert = Expert.objects.get(id = expert_id)
    except:
        return render(request, 'expert_error_detail.html', context)
    
    program_list = expert.selected_program_list
    return render(request, 'expert_detail.html', program_list)

def save_expert_req(request):

    if request.method == "POST":
        print("POST")
        form = ExpertForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("成功添加专家信息")
            form.save()
        else:
            print("添加失败，专家信息校验失败")
    # TODO: 后期添加成功后 跳转到专家详情页面。
    return redirect("/experts/list")