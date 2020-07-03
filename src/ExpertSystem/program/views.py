import os
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.http import FileResponse

from django.shortcuts import render



from experts.models import Expert
from program.models import Program
from program.forms import ProgramForm
from program.models import Program 

def program_list(request):
    
    program_list = Program.objects.all()
    return render(request, 'program_list_template.html', {"program_list": program_list})

def program_detail(request, program_id):
    try:
        program_detail_info = Program.objects.get(id=program_id)
    except:
        return HttpResponse("项目不存在， ID:", program_id)
    
    
    expert_list = Expert.objects.filter(selected_program_list__id=program_id)
    
    print(program_detail_info)
    print(expert_list)
    
    
    return render(request, 'program_detail.html', {"expert_list" : expert_list, "program": program_detail_info})

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
    
    print(id)
    print(context)
    
    
    return render(request, 'program_detail.html', {"expert_list" : expert_list, "program": context})

def program_check(request):
    return render(request, 'program_check_template.html')
    
def program_select_experts(request, id):
    """
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
    """
    """
    degree_dict = {"benke":"本科"， "shuoshi":"硕士", "boshi":"博士", "boshihou":"博士后"}
    """
    program = Program.objects.get(id=id)
    if request.method == 'GET':    
        return render(request, 'select_expert_template.html', {"program": program})
    if request.method == 'POST':
        level = request.POST.get('level')
        print(level)
        degree = request.POST.get('degree')
        print(degree)
        program_type = request.POST.get('program_type')
        print(program_type)
        number = request.POST.get('number')
        print(number)
        return render(request, 'select_expert_template.html', {"program": program, "level":level, "degree":degree, "program_type":program_type,"number":number})
    
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
        program_description = request.POST.get('remarks')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        program_date = request.POST.get('program_date')
        remarks = request.POST.get('remarks')
        new_program = Program(name= program_name,seq=program_seq,responser=program_responser,location=program_location,start_date=start_date,end_date=end_date,program_date=program_date,desp=remarks)
        new_program.save()
  
        program_list = Program.objects.all()
        
        return render(request, 'program_list_template.html', {"program_list":program_list})
    
    
def program_delete(request, id):    
    Program.objects.filter(id=id).delete()
    program_list = Program.objects.all()
    return render(request, 'program_list_template.html', {"program_list": program_list})

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

        program_list = Program.objects.all()
        return render(request, "program_list_template.html",{"program_list":program_list})
        
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
