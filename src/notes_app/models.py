from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ordered_model.models import OrderedModel
from django_bleach.models import BleachField
class Note(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=100)
    #intro starts here (single page)
    problem = models.TextField(blank=True)
    problem_solve = models.TextField(blank=True)
    how_problem_solved = models.TextField(blank=True)
    #intro ends here
    #project meta starts here (single page)
    difficulty = models.CharField(blank=True, max_length=100)
    prerequisites = models.TextField(blank=True)
    components = models.TextField(blank=True)
    #project meta ends here
    #steps
    step_title = models.CharField(blank=True, max_length=100)
    the_end = models.TextField(blank=True)
    cost = models.CharField(blank=True, max_length=100)
    purchase_places = models.TextField(blank=True)
    tools_using = models.TextField(blank=True)
    slug    = models.SlugField(null=True , blank=True)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active  = models.BooleanField(default=True)
    tags    = models.CharField(blank=True, max_length=100)
    code = models.FileField(upload_to='document' , blank=True)

    def __str__(self):
        return self.title

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Note , self).save(*args , **kwargs)

class Steps(models.Model):
    step_title = models.CharField(blank=True, max_length=100)
    step_photo = models.FileField(upload_to='media' , blank=True)
    step_photo_caption = models.CharField(blank=True, max_length=100)
    step_content = models.TextField(blank=True)
