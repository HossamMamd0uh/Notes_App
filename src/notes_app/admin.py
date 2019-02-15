from django.contrib import admin
from .models import Note , Steps , Story , About , News
# Register your models here.
admin.site.register(Note)
admin.site.register(Steps)
admin.site.register(Story)
admin.site.register(About)
admin.site.register(News)
