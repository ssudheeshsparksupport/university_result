from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.OneToOneField(User)
    firstname=models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

class Student(models.Model):
    
    registernum = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    DEPARTMENT_CHOICES = (
        ('IT', 'IT'),
        ('CS', 'CS'),
    )
    department = models.CharField(max_length=10, choices= DEPARTMENT_CHOICES)
    def __unicode__(self):
        return self.name

class Result(models.Model):
    mark = models.ForeignKey(Student)
    regnum = models.CharField(max_length=100)
    SEMESTER_CHOICES = (
        ('1', 'One'),
        ('2', 'Two'),
    )
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)

    YEAR_CHOICES = (
        ('2014', '2014'),
        ('2013', '2013'),
    )
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)

    SUBJECT_CHOICES = (
        ('Python', 'Python'),
        ('Java', 'Java'),
    )
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)

    mark = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

    def __unicode__(self):
        return self.regnum