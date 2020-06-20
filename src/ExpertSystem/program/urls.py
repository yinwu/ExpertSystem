from django.urls import path

from . import views

urlpatterns = [
    path('list', views.program_list, name='index'),
    path('detail/<int:id>', views.program_detail, name='detail'),
]