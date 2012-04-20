from django.db import models
# Create your models here.


class Movies(models.Model):
    favorite_movie = models.CharField(max_length=30)
    userid = models.ForeignKey('userinfo.User')
    def __unicode__(self):
        return self.favorite_movie