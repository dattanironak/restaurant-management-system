from django.db import models


# Create your models here.
class feedback(models.Model):
    feedback_desc = models.TextField(max_length=400)
    ratings = models.IntegerField()
    date = models.DateTimeField('date_recieved')
