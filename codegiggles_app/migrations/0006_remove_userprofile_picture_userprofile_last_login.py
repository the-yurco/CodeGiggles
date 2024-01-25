# Generated by Django 4.2.5 on 2024-01-20 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codegiggles_app', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
