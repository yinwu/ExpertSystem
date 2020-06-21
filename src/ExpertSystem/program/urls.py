from django.urls import path

from . import views

urlpatterns = [
    path('list', views.program_list, name='index'),
    path('add', views.program_add, name='add'),
    path('detail/<int:id>', views.program_detail, name='detail'),
]