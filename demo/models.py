from django.db import models

class Newsletter(models.Model):
    plainText = models.CharField(max_length=1000)
    html = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.plainText