from django.db import models
from userinfo.models import User

# Create your models here.

class UserLikesFood(models.Model):
    def __unicode__(self):
        return self.favoriteFood
    userid = models.ForeignKey('userinfo.User')
    favoriteFood = models.CharField(max_length=100)
