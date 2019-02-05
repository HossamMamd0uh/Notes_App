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
    note_id = models.AutoField(primary_key=True , null=False)
    title = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True , blank=True)
    about = models.TextField(blank=True)
    problem = models.TextField(blank=True)
    problem_solve = models.TextField(blank=True)
    how_problem_solve = models.TextField(blank=True)
    project_cost = models.IntegerField(blank=True, null=True)
    purchase_place = models.TextField(blank=True)
    tools_usage = models.TextField(blank=True)
    the_end = models.TextField(blank=True)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active  = models.BooleanField(default=True)
    tags    = models.CharField(blank=True, max_length=300)

    def __str__(self):
        return self.title

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Note , self).save(*args , **kwargs)

class Steps(models.Model):
    step_assign = models.ForeignKey(Note , on_delete=models.CASCADE)
    slug = models.SlugField(null=True , blank=True)
    step_title = models.CharField(blank=True, max_length=100)
    step_photo = models.FileField(upload_to='media' , blank=True)
    step_photo_caption = models.CharField(blank=True, max_length=100)
    step_content = models.TextField(blank=True)
    code = models.FileField(upload_to='document', blank=True)

    def __str__(self):
        return self.step_title

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.step_title)
            super(Steps , self).save(*args , **kwargs)
