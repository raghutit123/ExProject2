from django.db import models

# Create your models here.

class Student(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50,null=False, blank=False)
    second_name = models.CharField(max_length=52,null=False, blank=False)
    image = models.ImageField(upload_to='myapp/images', default="")

    def __str__(self):
        return self.first_name