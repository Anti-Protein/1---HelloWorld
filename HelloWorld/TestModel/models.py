# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 此处定义数据库的表结构，Django默认会自动加入id作为主键
# 修改表结构后
# python manage.py makemigrations TestModel #让Django知道模型有变更
# python manage.py migrate TestModel        #创建表结构

# 第一次时 python manage.py migrate   # 创建表结构 ?

class Test(models.Model):
    name = models.CharField(max_length=20) 

class Contact(models.Model):
    name  = models.CharField(max_length=200) #存储字符串
    age   = models.IntegerField(default=0)   #存储整数
    email = models.EmailField()              #存储Email
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact) #将Contact作为外键
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

