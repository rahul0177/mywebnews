# Generated by Django 2.2.4 on 2019-09-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('news', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=40)),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
    ]
