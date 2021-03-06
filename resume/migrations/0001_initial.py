# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-14 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('0', '女'), ('1', '男')], max_length=1, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('address', models.CharField(max_length=30, verbose_name='住址')),
                ('school', models.CharField(max_length=50, verbose_name='毕业学校')),
                ('experience', models.TextField(verbose_name='工作经历')),
                ('evaluation', models.TextField(verbose_name='自我评价')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Candidaters')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_id', models.IntegerField()),
                ('zhaopin_id', models.IntegerField()),
                ('rec_id', models.IntegerField()),
                ('createdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
