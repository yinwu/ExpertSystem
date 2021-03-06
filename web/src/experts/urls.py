from django.urls import path



from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('login_out/', views.login_out_user, name='login'),
    path('index/', views.index, name='index'),
    path('list/', views.expert_list, name='list'),
    path('detail/<int:expert_id>', views.expert_detail, name='detail'),
    path('add', views.add_expert_req, name='addExpert'),
    path('deleteExpert/<int:expert_id>', views.delete_expert_req, name='deleteExpert'),
    path('modify/<int:expert_id>', views.modify_expert_req, name='modify'),
    path('search/', views.search, name='search'),
    path('comments/<int:expert_id>/<int:program_id>', views.comments, name='comments'),  
    path('loginValidation/', views.login_validation, name='loginValidation'),
    path('importExperts', views.import_experts, name='importExperts'),
]
