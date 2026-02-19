from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

       
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")

        return redirect('contact')

    return render(request, "contact.html")
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email to Admin
        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        # Send confirmation to User
        send_mail(
            subject="Thank you for contacting Rakesh Yadav",
            message="Your message has been received. I will contact you soon.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, "contact.html")
