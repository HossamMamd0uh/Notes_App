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
