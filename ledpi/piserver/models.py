from django.utils import timezone
from django.db import models
import datetime


# Create your models here.
class Lights(models.Model):
    light_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.light_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    light = models.ForeignKey(Lights, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    on  = models.IntegerField(default=0)
    off = models.IntegerField(default=1)

    def __str__(self):
        return self.choice_text
