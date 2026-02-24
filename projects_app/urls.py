from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:id>/', views.project_detail, name='project_detail'),
    path('create/', views.create_project, name='create_project'),
    path('edit/<int:id>/', views.edit_project, name='edit_project'),
    path('delete/<int:id>/', views.delete_project, name='delete_project'),
]
