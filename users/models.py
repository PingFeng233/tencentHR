from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class Candidaters(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password1 = models.CharField(max_length=128, verbose_name='密码')
    password2 = models.CharField(max_length=128, verbose_name='密码确认')
    tel = models.CharField(max_length=20, verbose_name='手机')
    email = models.EmailField(verbose_name='邮箱')
    headshot = models.ImageField(upload_to='avatar/%Y/%m/%d', default='default.jpg',
                                 verbose_name='头像', null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password1 = self.password2 = set_password(self.password1)
        super(Candidaters, self).save(*args, **kwargs)


class Recruiter(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password1 = models.CharField(max_length=128, verbose_name='密码')
    password2 = models.CharField(max_length=128, verbose_name='密码确认')
    tel = models.CharField(max_length=20, verbose_name='手机')
    email = models.EmailField(verbose_name='邮箱')
    department = models.CharField(max_length=30, verbose_name='部门', null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password1 = self.password2 = set_password(self.password1)
        super(Recruiter, self).save(*args, **kwargs)


def set_password(password):
    # 设置密码
    password_hash = make_password(password)
    return password_hash


def check_password_hash(password, password_hash):
    return check_password(password, password_hash)
