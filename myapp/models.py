from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=250)
    client_name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name
    
class Package(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='packages/')

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    education = models.CharField(max_length=250)
    image = models.ImageField(upload_to='team_members/', default='images/individuals.png')

    def __str__(self):
        return self.name