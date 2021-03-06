# Generated by Django 2.0.2 on 2019-01-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0020_auto_20190124_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='circuit',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='circuit_problem',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='circuit_schema',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='components',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='cost',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='note',
            name='difficulty',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='note',
            name='how_problem_solved',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='prerequisites',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='problem',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='problem_solve',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='purchase_places',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='the_end',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='tools_using',
            field=models.TextField(blank=True),
        ),
    ]
