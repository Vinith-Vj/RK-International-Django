from django.contrib import admin

from .models import Project, Package, TeamMember

# Register your models here.

admin.site.register(Project)

admin.site.register(Package)

admin.site.register(TeamMember)