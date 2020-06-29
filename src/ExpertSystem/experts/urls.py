from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.expert_list, name='list'),
    path('detail/<int:expert_id>', views.expert_detail, name='detail'),
    path('add/', views.add_expert_req, name='addExpert'),
    path('deleteExpert/', views.delete_expert_req, name='deleteExpert'),
    path('save/', views.save_expert_req, name='save'),
]
