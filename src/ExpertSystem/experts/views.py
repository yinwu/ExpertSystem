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

    
def delete_expert_req(request):
    return render(request, 'delete_expert_template.html')

def add_expert_req(request):
    expert_form = ExpertForm()
    return render(request, 'add_expert_template.html', {"expert_form": expert_form})

def expert_detail(request, expert_id):

    try:
        expert = Expert.objects.get(id = expert_id)
    except:
        return HttpResponse("专家不存在，ID:", expert_id)
    
    program_list = expert.selected_program_list
    return render(request, 'expert_detail.html', {"expert":expert})

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
