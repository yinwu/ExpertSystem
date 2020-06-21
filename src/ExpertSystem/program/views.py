from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from experts.models import Expert
from program.models import Program

def program_list(request):
    
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
    program_list = Program.objects.all()
    return render(request, 'program_list_template.html', {"result": program_list, "program_list": test_data})

def program_detail(request, id):

    expert_list = [
        {"name":"张三", "title":"院士", "unit":"北航", "phone":"18788878781", "level":"高级"},
        {"name":"李四", "title":"院士", "unit":"北航", "phone":"18788878782", "level":"高级"},
        {"name":"李四", "title":"院士", "unit":"北航", "phone":"18788878783", "level":"高级"},
        {"name":"李四", "title":"院士", "unit":"北航", "phone":"18788878784", "level":"高级"},
        {"name":"李四", "title":"院士", "unit":"北航", "phone":"18788878785", "level":"高级"},
        {"name":"李四", "title":"院士", "unit":"北航", "phone":"18788878786", "level":"高级"},
        {"name":"李四", "title":"院士", "unit":"北航", "phone":"18788878787", "level":"高级"},
        {"name":"李四", "title":"院士", "unit":"北航", "phone":"18788878788", "level":"高级"},
        {"name":"李四", "title":"院士", "unit":"北航", "phone":"18788878789", "level":"高级"},
        {"name":"李四", "title":"院士", "unit":"北航", "phone":"187888787810", "level":"高级"}
    ]
    
    return render(request, 'program_detail.html', {"expert_list" : expert_list})


def program_add(request):
    return render(request, 'add_program_template.html')

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