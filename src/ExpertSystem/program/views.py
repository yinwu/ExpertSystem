from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from experts.models import Expert

def program_list(request):
    
    program_list = Program.objects.all()
    return render(request, 'program_list_template.html', {"result": program_list})

def program_detail(request, program_id):
    
    return render(request, 'program_detail_template.html', context)


def get_experts_list(program_id):
    experts = Expert.objects.filter(program__id=program_id)
    return experts

def get_available_experts(program_id, num):
    program = Program.objects.get(id=program_id)

    selected_expert = program.selected_experts
    exclued_expert = program.exclued_expert

    count = Expert.objects.count()
    if num >= count:
        return Expert.objects.filter()

    pass