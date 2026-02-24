from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Project


# ===============================
# PUBLIC VIEWS
# ===============================

def project_list(request):
    projects = Project.objects.order_by('-created_date')
    return render(request, 'projects.html', {'projects': projects})


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project_detail.html', {'project': project})


# ===============================
# ADMIN CHECK
# ===============================

def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)


# ===============================
# CREATE PROJECT
# ===============================

@admin_required
def create_project(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        tech_stack = request.POST.get("tech_stack")
        github = request.POST.get("github_link")
        linkedin = request.POST.get("linkedin_link")
        thumbnail = request.FILES.get("thumbnail")

        Project.objects.create(
            title=title,
            description=description,
            tech_stack=tech_stack,
            github_link=github,
            linkedin_link=linkedin,
            thumbnail=thumbnail
        )

        messages.success(request, "Project created successfully.")
        return redirect('project_list')

    return render(request, "create_project.html")


# ===============================
# DELETE PROJECT
# ===============================

@admin_required
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect('project_list')


# ===============================
# EDIT PROJECT
# ===============================

@admin_required
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.tech_stack = request.POST.get('tech_stack')
        project.github_link = request.POST.get('github_link')
        project.linkedin_link = request.POST.get('linkedin_link')

        if request.FILES.get('thumbnail'):
            project.thumbnail = request.FILES.get('thumbnail')

        project.save()
        return redirect('project_list')

    return render(request, 'edit_project.html', {'project': project})