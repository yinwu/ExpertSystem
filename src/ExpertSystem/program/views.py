from django.shortcuts import render
import os

# Create your views here.

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.http import FileResponse

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
    
    
   
    context = {}
    context = test_data[id-1]
    
    print(id)
    print(context)
    
    
    return render(request, 'program_detail.html', {"expert_list" : expert_list, "program": context})

def program_check(request):
    return render(request, 'program_check_template.html')
    
def program_select_experts(request, id):
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
    
    
   
    context = {}
    context = test_data[id-1]
    return render(request, 'select_expert_template.html', {"program": context})
    
def program_export_experts(request, id):
    return render(request, 'export_expert_template.html')


def program_add(request):
    if request.method == 'GET':
        return render(request, 'add_program_template.html')
    
    if request.method == 'POST':
        test_data2 = [
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
        program_name = request.POST.get('name')
        program_responser = request.POST.get('responser')
        program_description = request.POST.get('remarks')
        next_index = len(test_data2)+1
        program_item = {"id":"", "name":"", "responser":"", "description":"", "info":""}
        program_item['id'] = next_index
        program_item['name'] = program_name
        program_item['responser'] = program_responser
        program_item['description'] = program_description
        test_data2.append(program_item)
        print("I come to POST")
        program_list = Program.objects.all()
        
        return render(request, "delete_program_template.html",{"program_list":test_data2})
    
def program_delete(request, id):
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
  
    test_data.pop(id-1)
    program_list = Program.objects.all()
    return render(request, 'delete_program_template.html', {"program_list": test_data})
    
    

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
    keyStr = request.GET.get('name')
    post_list = []
    
    for item in test_data:
        if item['name'] == keyStr:
            post_list.append(item) 
    return render(request, 'program_list_search.html', {'post_list': post_list})
    
     
    
def program_modify(request, id):
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
    if request.method == 'GET':
        item = {}
        item = test_data[id-1]
        return render(request, 'modify_program_template.html', {"program_item": item, "program_id": id})
        
    if request.method == 'POST':
        test_data2 = [
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
    
        program_name = request.POST.get('name')
        program_responser = request.POST.get('responser')
        program_description = request.POST.get('remarks')
        program_item = {}
        program_item = test_data2[id-1]
        program_item['name'] = program_name
        program_item['responser'] = program_responser
        program_item['description'] = program_description
        test_data2.pop(id-1)
        test_data2.insert(id-1, program_item)
        print("this is my print debug in post")
    
        program_list = Program.objects.all()
        
        return render(request, "delete_program_template.html",{"program_list":test_data2})
        
def download_table(request, id):
    file_name = 'expertfile/test_' + str(id) + '.xlsx'
    file_path = os.path.join(os.getcwd(), file_name)
    if os.path.exists(file_path):
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="mytest.xlsx"'
        return response

    else:

        raise Http404
        
def program_save(request):
    
    
    test_data2 = [
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
    if request.method == 'POST':
        program_name = request.POST.get('name')
        program_responser = request.POST.get('responser')
        program_description = request.POST.get('remarks')
        program_item = {}
        program_item = test_data2[0]
        program_item['name'] = program_name
        program_item['responser'] = program_responser
        program_item['description'] = program_description
        test_data2.append(item)
        print("I come to POST")
    program_list = Program.objects.all()
        
    return render(request, "delete_program_template.html",{"program_list":test_data2})
    
    
    
    
