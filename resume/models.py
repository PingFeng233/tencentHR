from django.db import models


# Create your models here.
class Resume(models.Model):
    sex = (
        ('0', '女'),
        ('1', '男')
    )
    name = models.CharField(verbose_name='姓名', max_length=20)
    sex = models.CharField(max_length=1, verbose_name='性别', choices=sex)
    age = models.IntegerField(verbose_name='年龄')
    address = models.CharField(max_length=30, verbose_name='住址')
    school = models.CharField(max_length=50, verbose_name='毕业学校')
    experience = models.TextField(verbose_name='工作经历')
    evaluation = models.TextField(verbose_name='自我评价')
    user = models.OneToOneField('users.Candidaters', unique=True)

    def __str__(self):
        return self.name


class Resume_relationship(models.Model):
    resume_id = models.IntegerField()
    zhaopin_id = models.IntegerField()
    rec_id = models.IntegerField()
    createdate = models.DateTimeField(auto_now_add=True)
