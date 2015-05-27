from django.db import models
from django.utils import timezone
# Create your models here.

    class UserForm(models.Model):
        user = models.ForeignKey(User)
        portrait = models.ImageField(upload_to = 'static/img')
        nickname = models.CharField(max_length=50)
        signature = models.CharField(max_length=225)



    class Userauth(models.Model):
        user = models.OneToOneField(UserForm)

        email = models.CharField(max_length=100)
        cellphone = models.CharField(max_length=15)
        weiboname = models.CharField(max_length=100)



class Shirt(models.Model):
    sid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to = 'poll/static/img')
    votenum = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Vote(models.Model):
    shirt = models.ForeignKey(Shirt)
    studentname = models.CharField(max_length=10)
    studentnumber = models.IntegerField()
    vote_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.studentname + repr(self.studentnumber)