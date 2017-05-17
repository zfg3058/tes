#coding: utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
role_ite = (
    (1,'admin'),
    (2,'system'),
    (3,'customer'),
    (0,'commonly')
)

class UserCount(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=20, null=False, blank=False)
    passwd = models.CharField(max_length=20, null=False, blank=False)
    role = models.IntegerField(choices=role_ite, default=0)
    rgtime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Asset(models.Model):
    asId = models.IntegerField(blank=False, null=False, default=0)
    statu = models.CharField(max_length=20, blank=False, null=True, default='', verbose_name=u"闲置")
    ip = models.CharField(max_length=32, blank=True, null=True, default='0.0.0.0')
    cpu = models.CharField(max_length=20, blank=False, null=False)
    ram = models.CharField(max_length=20, blank=False, null=True)
    YP = models.CharField(max_length=20, blank=False, null=True)
    TYPE = models.CharField(max_length=30, blank=True, null=True)
    remark = models.TextField(max_length=100, blank=True, null=True)
    bgtime = models.DateTimeField(auto_now=True,null=True)
    edtime = models.DateTimeField(auto_now_add=True,null=True)

    def __unicode__(self):
        return self.asId, self.statu

levels = (
    (1,u'一级用户'),
    (2,u'二级用户'),
    (3,u'三级用户'),
    (4,u'四级用户'),
    (0,u'未分配'),
)
class Users(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    level = models.CharField(max_length=20, choices=levels, null=True, default=0)
    assets = models.TextField(max_length=100, null=True, default='')
    remark = models.TextField(max_length=100, null=True, default='')

    def __unicode__(self):
        return self.name

class UserGroup(models.Model):
    level = models.CharField(max_length=20, choices=levels, null=True, default=0)
    remark = models.CharField(max_length=100, null=True, default='')
    time = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.level



