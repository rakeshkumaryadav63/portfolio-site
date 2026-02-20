from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from projects_app.models import Project
from .serializers import ProjectSerializer


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_date')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

from contact_app.models import ContactMessage
from .serializers import ContactSerializer
from django.core.mail import send_mail
from django.conf import settings


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        contact = serializer.save()

        send_mail(
            subject=f"New Contact Message from {contact.name}",
            message=contact.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        send_mail(
            subject="Thank you for contacting me",
            message="Your message has been received.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[contact.email],
        )

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_date')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'tech_stack']
    ordering_fields = ['created_date', 'title']