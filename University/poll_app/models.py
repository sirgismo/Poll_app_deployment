from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class userProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Instructors(models.Model):
    Email = models.EmailField(unique=True)
    FirstName = models.CharField(max_length= 50)
    LastName = models.CharField(max_length = 100)
    IsHead = models.BooleanField(default=False)

    def __str__(self):
        InstName = self.FirstName + " " +self.LastName + " " + self.Email
        if (self.IsHead == True):
            InstName =   self.FirstName + " " +self.LastName +" " + self.Email+ " " + "(H)"
        return InstName


class Questions(models.Model):

    Title = models.CharField(max_length = 50)
    Description = models.TextField()
    CreationDate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Title


class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    QID = models.IntegerField()
    userid = models.IntegerField()
    Description = models.TextField()
    CreationDate =models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Description
