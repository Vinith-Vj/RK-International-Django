from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=250)
    client_name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name