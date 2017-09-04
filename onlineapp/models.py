from __future__ import unicode_literals

# -*- coding: utf-8 -*-
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class College(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    acronym = models.CharField(max_length=8)
    contact = models.EmailField()

    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=128)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    db_folder = models.CharField(max_length=50)
    college = models.ForeignKey(College)
    dropped_out = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class MockTest1(models.Model):
    problem1 = models.IntegerField()
    problem2 = models.IntegerField()
    problem3 = models.IntegerField()
    problem4 = models.IntegerField()
    total = models.IntegerField()

    student = models.OneToOneField(Student)
# Create your models here.
#class College(models.Model):
 #   name=models.CharField(max_length=128)
  #  location=models.CharField(max_length=64)
   # acronym = models.CharField(max_length=8)
    #contact = models.EmailField()
    #def __unicode__(self):
     #   return self.name