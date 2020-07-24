from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('list', views.program_list, name='index'),
    path('add', views.program_add, name='add'),
    path('save', views.save_program, name='save'),
    path('add', views.program_add, name='addProgram'),
    path('deleteProgram/<int:id>', views.program_delete, name='deleteProgram'),
    path('detail/<int:program_id>', views.program_detail, name='detail'),
    path('checkProgram', views.program_check, name='checkProgram'),
    path('selectExperts/<int:id>', views.program_select_experts, name='selectExperts'),
    path('exportExperts/<int:id>', views.program_export_experts, name='exportExperts'),
    path('search/', views.search, name='search'),
    path('modify/<int:id>', views.program_modify, name='modifyProgram'),
    path('confirm/<int:expert_id>/<int:program_id>', views.expert_confirm, name='confirm'),
    path('exclude/<int:expert_id>/<int:program_id>', views.expert_exclude, name='exclude'),
]
