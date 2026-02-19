from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('create/', views.create_project, name='create_project'),

]
