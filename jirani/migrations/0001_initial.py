# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-19 12:48
from __future__ import unicode_literals

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
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('neighbourhood_logo', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('healthcenter_number', models.IntegerField(blank=True, null=True)),
                ('police_number', models.IntegerField(blank=True, null=True)),
                ('occupants_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('post', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='jirani.Neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('bio', models.TextField(blank=True, max_length=254)),
                ('profile_picture', models.ImageField(default='default.png', upload_to='images/')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('neighbourhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='jirani.Neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='jirani.Profile'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='jirani.Profile'),
        ),
        migrations.AddField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='jirani.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='jirani.Profile'),
        ),
    ]
