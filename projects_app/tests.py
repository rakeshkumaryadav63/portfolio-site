from django.test import TestCase
from .models import Project

class ProjectModelTest(TestCase):
    def test_project_creation(self):
        project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            tech_stack="Python"
        )
        self.assertEqual(project.title, "Test Project")
