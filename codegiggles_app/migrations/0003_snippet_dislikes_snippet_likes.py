# Generated by Django 4.2.5 on 2023-12-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codegiggles_app', '0002_snippet_description_alter_snippet_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='snippet',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]