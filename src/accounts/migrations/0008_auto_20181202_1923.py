# Generated by Django 2.0.2 on 2018-12-02 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20181202_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='الاسم_الاخير',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='الاسم_الاول',
        ),
    ]
