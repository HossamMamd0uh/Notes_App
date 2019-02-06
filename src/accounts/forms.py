from django import forms
from . import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username' ,
                   'first_name' ,
                   'last_name' ,
                   'email'
                   ]
        labels = {
                  'username' : _('اسم المستخدم'),
                  'first_name' : _('الاسم الاول'),
                  'last_name' : _('الاسم الاخير'),
                  'email' :_('البريد الالكتروني')
                  }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [ 'headline' , 'bio' , 'profile_img' , 'name']
        labels = {
                  'name' : _('الاسم'),
                  'headline' : _('المهارات'),
                  'bio' : _('نبذة عنك'),
                  'profile_img' : _('الصورة الشخصية'),
                  }
