from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
# from accounts.models import Profile
# Create your models here.

#master
class Course(models.Model):
    CHOICE = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    heading = models.CharField(max_length=200)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    rating = models.IntegerField(choices=CHOICE)
    description = models.TextField()
    instructor = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True)
    photo = models.FileField(upload_to='files', null=True, blank=True)

    def __str__(self):
        return f"{self.heading}"

class Topic(models.Model):
    heading = models.CharField(max_length=200)
    video = models.FileField(upload_to='files', null=True, blank=True)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='topics')
    time_required = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.heading}"

class MyCourse(models.Model):
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    progress = models.FloatField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.course.heading}"

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"