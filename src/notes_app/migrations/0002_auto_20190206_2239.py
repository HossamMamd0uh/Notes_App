# Generated by Django 2.0.2 on 2019-02-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='about_photo',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
