# Generated by Django 2.0.2 on 2019-04-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0007_note_diff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='about_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='note',
            name='comp_photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='note',
            name='fin_photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='note',
            name='tools_photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
