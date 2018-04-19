from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class WorkLocation(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Zhaopin(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='招聘要求')
    peopleNumber = models.IntegerField(verbose_name='人数')
    workLocation = models.ForeignKey(WorkLocation, verbose_name='工作地点')
    publishTime = models.DateField(auto_now_add=True, verbose_name='创建时间')
    category = models.ForeignKey(Category, verbose_name='类别')
    author = models.ForeignKey('users.Recruiter', verbose_name='作者', default='管理员')

    def __str__(self):
        return self.title
