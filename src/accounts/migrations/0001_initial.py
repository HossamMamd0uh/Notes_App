# Generated by Django 2.0.2 on 2019-02-10 20:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('headline', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('profile_img', models.ImageField(blank=True, upload_to='media')),
                ('register_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
