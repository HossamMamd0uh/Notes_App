from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    المستخدم = models.OneToOneField(User , on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    headline = models.CharField(blank=True, max_length=100)
    bio = models.TextField(blank=True)
    الصورة_الشخصية = models.ImageField(upload_to="profile_img" , blank=True)
    تاريخ_التسجيل = models.DateTimeField(blank=True, default=datetime.datetime.now , null=True)

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.المستخدم)
        super(Profile , self).save(*args , **kwargs)


    def __str__(self):
        return '%s' %(self.المستخدم)


def create_profile(sender , **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(المستخدم=kwargs['instance'])

post_save.connect(create_profile,sender=User)
