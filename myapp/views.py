from django.shortcuts import render
from .models import Project, Package
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):

    projects = Project.objects.all()
    all_packages = Package.objects.all()

    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        number = request.POST['number']

        send_mail(
            'Contact Form',
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
    return render(request, 'index.html', {'projects': projects, 'packages': all_packages})

