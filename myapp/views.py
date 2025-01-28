from django.shortcuts import render
from .models import Project, Package

# Create your views here.

def index(request):
    projects = Project.objects.all()
    all_packages = Package.objects.all()
    return render(request, 'index.html', {'projects': projects, 'packages': all_packages})

