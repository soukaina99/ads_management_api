from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ad(models.Model):
    #  a basic model for ads
    title = models.CharField("title",max_length=255)
    image = models.ImageField('Photo',upload_to='ads/photo',blank=True)
    description = models.TextField('Description',blank=True)

    def __unicode__(self):
        return u'%s' % self.title


class UserAd(models.Model):
    # a class relating the user with his ads
    # using the default django user model

    AUTO_SAVE = 0
    MANUAL_SAVE = 1
    AD_TYPES = (
        (AUTO_SAVE, 'Auto save'),
        (MANUAL_SAVE, "Manual save")
    )
    user = models.ForeignKey(User)
    ad = models.ForeignKey(Ad)
    ad_type = models.IntegerField("Ad Type",choices=AD_TYPES)
    added_at = models.DateTimeField('Added at',auto_now_add=True)
