# Generated by Django 2.0.2 on 2019-02-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='project_cost',
            field=models.TextField(blank=True, null=True),
        ),
    ]
