from discord import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse   # get absolute GET method for redirects

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # User to POST - 1:n cardianality
# Querying models in django shell will return this model with the name as defined below i.e. title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        #return reverse('post-detail', kwargs={'pk':self.pk})