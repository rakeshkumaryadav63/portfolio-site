from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect('dashboard')

    return render(request, 'signup.html')
from django.contrib.auth.decorators import login_required
from projects_app.models import Project
from contact_app.models import ContactMessage
from django.shortcuts import render


@login_required
def dashboard(request):

    total_projects = Project.objects.count()
    total_messages = ContactMessage.objects.count()

    recent_projects = Project.objects.order_by('-created_date')
    recent_messages = ContactMessage.objects.order_by('-timestamp')

    context = {
        'total_projects': total_projects,
        'total_messages': total_messages,
        'recent_projects': recent_projects,
        'recent_messages': recent_messages,
    }

    return render(request, 'dashboard.html', context)