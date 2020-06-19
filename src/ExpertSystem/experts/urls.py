from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.expert_list, name='index'),
    path('detail/', views.expert_detail, name='detail'),
]