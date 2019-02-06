from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    headline = models.CharField(blank=True, max_length=100)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to="media" , blank=True)
    register_date = models.DateTimeField(blank=True, default=datetime.datetime.now , null=True)

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Profile , self).save(*args , **kwargs)


    def __str__(self):
        return '%s' %(self.user)


def create_profile(sender , **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)
