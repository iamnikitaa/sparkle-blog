from django.db import models
from django.utils import timezone
from django.urls import  reverse
from django.contrib.auth.models import User

#if we want to see the sqlcode we can run python manage.py sqlmigrate blog 0001 to see the code

class Post(models.Model):  
    title = models.CharField(max_length=100)  
    content = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})