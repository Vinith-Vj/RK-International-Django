from django.shortcuts import render, redirect
from .models import Project, Package, TeamMember
from django.core.mail import send_mail 
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index(request):

    projects = Project.objects.all()
    all_packages = Package.objects.all()
    team_members = TeamMember.objects.all()

    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        number = request.POST['number']

        # send_mail(
        #     'New Contact Form Submission',
        #     f"Name: {name}\nContact Number: {number}\nEmail: {email}\nMessage: {message}",
        #     settings.EMAIL_HOST_USER,
        #     [settings.EMAIL_HOST_USER], 
        #     fail_silently=False
        # )

        subject = 'New Contact Form Submission'
        body = f"""
        Name: {name}
        Contact Number: {number}
        Email: {email}
        Message: {message}
        """
        sender_email = email  # 👈 The user's email as the sender
        recipient_email = [settings.EMAIL_HOST_USER]  # 👈 Send to your email

        send_mail(
            subject,
            body,
            sender_email,  # 👈 This is the key change (User's email as sender)
            recipient_email,
            fail_silently=False
        )

        return redirect('index')
    return render(request, 'index.html', {'projects': projects, 'packages': all_packages, 'team_members': team_members})

