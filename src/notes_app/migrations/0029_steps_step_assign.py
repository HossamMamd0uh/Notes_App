# Generated by Django 2.0.2 on 2019-02-04 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0028_auto_20190203_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='steps',
            name='step_assign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notes_app.Note'),
        ),
    ]
