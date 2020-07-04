from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.expert_list, name='list'),
    path('detail/<int:expert_id>', views.expert_detail, name='detail'),
    path('add/', views.add_expert_req, name='addExpert'),
    path('deleteExpert/<int:expert_id>', views.delete_expert_req, name='deleteExpert'),
    path('modify/<int:expert_id>', views.modify_expert_req, name='modify'),
    path('search/', views.search, name='search'),
]
