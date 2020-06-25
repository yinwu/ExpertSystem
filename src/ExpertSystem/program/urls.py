from django.urls import path

from . import views

urlpatterns = [
    path('list', views.program_list, name='index'),
    path('add', views.program_add, name='addProgram'),
    path('deleteProgram', views.program_delete, name='deleteProgram'),
    path('detail/<int:id>', views.program_detail, name='detail'),
    path('checkProgram', views.program_check, name='checkProgram'),
    path('selectExperts/<int:id>', views.program_select_experts, name='selectExperts'),
    path('exportExperts/<int:id>', views.program_export_experts, name='exportExperts'),
]