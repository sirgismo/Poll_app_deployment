# Generated by Django 3.0.3 on 2020-09-06 10:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('QID', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('Description', models.TextField()),
                ('CreationDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=100)),
                ('IsHead', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('CreationDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='userProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
