from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    #userId = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    Faculty = models.ForeignKey(User, limit_choices_to={'groups__name': 'Faculty'}, on_delete=models.CASCADE)
    #userId = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    reviewText = models.TextField(max_length=500, blank=False)
    timeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):#for python <2
        return self.name

    def __str__(self):#for python 3
        return self.name
