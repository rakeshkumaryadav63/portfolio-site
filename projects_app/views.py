from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.order_by('-created_date')
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@admin_required
def create_project(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        tech_stack = request.POST.get("tech_stack")
        github = request.POST.get("github_link")
        live = request.POST.get("live_demo_link")

        Project.objects.create(
            title=title,
            description=description,
            tech_stack=tech_stack,
            github_link=github,
            live_demo_link=live
        )

        messages.success(request, "Project created successfully.")
        return redirect('project_list')

    return render(request, "create_project.html")
