# Generated by Django 2.0.2 on 2019-02-03 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0027_auto_20190203_1340'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Step4',
            new_name='Steps',
        ),
        migrations.DeleteModel(
            name='Step1',
        ),
        migrations.DeleteModel(
            name='Step10',
        ),
        migrations.DeleteModel(
            name='Step2',
        ),
        migrations.DeleteModel(
            name='Step3',
        ),
        migrations.DeleteModel(
            name='Step5',
        ),
        migrations.DeleteModel(
            name='Step6',
        ),
        migrations.DeleteModel(
            name='Step7',
        ),
        migrations.DeleteModel(
            name='Step8',
        ),
        migrations.DeleteModel(
            name='Step9',
        ),
    ]
