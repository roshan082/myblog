# path() --> takes 3 parameter
# 1. urls --> "<url_name/>"
# 2. views and function name --> <views.function_name>
# 3. name --> name = "<url_name>" -- this is optional


from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo, name = 'demo'),
    path('register/', views.register, name= 'user.register'),
    path('edit/<int:id>/', views.user_edit, name='user.edit'),
    path('show/<int:id>/', views.user_show, name='user.show'),
    path('login/', views.user_login, name='user.login'),
    path('dashboard/', views.user_dashboard, name='user.dashboard'),
    path('logout/', views.user_logout, name='user.logout'),


    # CRUD
    # Create, Retrive( list, single ), Update, Delete
    # post Urls
    path('posts/', views.post_index, name='posts.index'),
    path('posts/edit/<int:post_id>', views.post_edit, name='posts.edit'),
    path('posts/show/<int:post_id>', views.post_show, name='posts.show'),
    path('posts/delete/<int:post_id>', views.post_delete, name='posts.delete'),
    path('posts/create/', views.post_create, name='posts.create'),
    path('posts/update/', views.post_update, name='posts.update'),
    # path('posts/edit/<int:post_id>', views.post_edit, name='posts.edit'),

]