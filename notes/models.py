
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Note(models.Model):
    title  = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=True,null = False)
    date = models.DateTimeField( auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('detail', kwargs = {'pk': self.pk})
