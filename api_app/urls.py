from django.urls import path
from .views import (
    ProjectListAPIView,
    ProjectDetailAPIView,
    ProjectCreateAPIView,
    ContactCreateAPIView,
)

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='api_projects'),
    path('projects/<slug:slug>/', ProjectDetailAPIView.as_view(), name='api_project_detail'),
    path('projects/create/', ProjectCreateAPIView.as_view(), name='api_project_create'),
    path('contact/', ContactCreateAPIView.as_view(), name='api_contact'),
]
