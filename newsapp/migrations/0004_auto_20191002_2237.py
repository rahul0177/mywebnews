# Generated by Django 2.2.4 on 2019-10-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_headnews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='images',
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='news',
            name='published',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
