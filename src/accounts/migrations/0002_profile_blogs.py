# Generated by Django 2.0.2 on 2019-03-31 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0005_news'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blogs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notes_app.Note'),
        ),
    ]
