from rest_framework import generics, permissions
from projects_app.models import Project
from contact_app.models import ContactMessage
from .serializers import ProjectSerializer, ContactSerializer


# GET all projects
class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_date')
    serializer_class = ProjectSerializer


# GET single project by slug
class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


# POST new project (Admin only)
class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


# POST contact message
class ContactCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
