from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from experts.models import *


def index(request):
    return render(request, 'index.html')

def expert_list(request):
    expert_list = Expert.objects.all()
    return render(request, 'expert_list_template.html', {"result":expert_list})


def add_expert_req(request):
    return render(request, 'add_program_template.html')

def expert_detail(request, expert_id):
    context = {"name":"test_name"}

    try:
        expert = Expert.objects.get(id = expert_id)
    except:
        return render(request, 'expert_error_detail.html', context)
    
    program_list = expert.selected_program_list
    return render(request, 'expert_detail.html', program_list)