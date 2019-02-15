from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
from ckeditor.fields import RichTextField
from ordered_model.models import OrderedModel
from django_bleach.models import BleachField
from django.dispatch import receiver
from .slugify import unique_slug_generator
from django.utils.text import slugify


class Note(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=100)
    featured_photo = models.FileField(upload_to='media' , blank = True)
    slug    = models.SlugField(null=True , blank=True , allow_unicode=True, unique=True)
    about = models.TextField(blank=True)
    about_photo = models.FileField(upload_to='media' , blank=True , null=True)
    vid = models.FileField(upload_to='media' , blank=True)
    comp = models.TextField(blank=True)
    comp_photo = models.FileField(upload_to='media' , blank=True)
    tools = models.TextField(blank=True)
    tools_photo = models.FileField(upload_to='media' , blank=True)
    project_cost = models.TextField(blank=True, null=True)
    purchase_place = models.TextField(blank=True)
    tools_usage = models.TextField(blank=True)
    the_end = models.TextField(blank=True)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active  = models.BooleanField(default=True)
    tags    = models.CharField(blank=True, max_length=300)
    poject_code = models.FileField(upload_to ='document' , blank=True)
    code_link = models.URLField(max_length=500 , blank=True)
    fin_photo = models.FileField(upload_to='media' , blank=True)
    fin_vid = models.URLField(max_length=500 , blank=True)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Note.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class Steps(models.Model):
    step_assign = models.ForeignKey(Note , on_delete=models.CASCADE)
    slug = models.SlugField(null=True , blank=True)
    title = models.CharField(blank=True, max_length=100)
    step_photo = models.FileField(upload_to='media' , blank=True)
    step_photo_caption = models.CharField(blank=True, max_length=100)
    step_content = models.TextField(blank=True)
    code = models.FileField(upload_to='document', blank=True)
    step_code = models.FileField(upload_to='document', blank=True)
    step_code_link = models.URLField(max_length=500 , blank=True)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Note.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class Story(models.Model):
    user  = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=100)
    slug  = models.SlugField(null=True , blank=True)
    story_photo = models.FileField(upload_to='media' , blank=True)
    story_photo_caption = models.CharField(blank=True, max_length=100)
    story_content = RichTextField()
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)


def __str__(self):
    return self.title

def _get_unique_slug(self):
    slug = slugify(self.title)
    unique_slug = slug
    num = 1
    while Note.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = self._get_unique_slug()
    super().save(*args, **kwargs)

class About(models.Model):
    user  = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=100)
    slug  = models.SlugField(null=True , blank=True)
    about_photo = models.FileField(upload_to='media' , blank=True)
    about_content = RichTextField()
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Note.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class News(models.Model):
    user  = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=100)
    slug  = models.SlugField(null=True , blank=True)
    news_photo = models.FileField(upload_to='media' , blank=True)
    news_content = RichTextField()
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Note.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
