# Generated by Django 4.2.5 on 2023-12-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codegiggles_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(max_length=50),
        ),
    ]
