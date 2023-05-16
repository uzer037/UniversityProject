from django.db import models

# Create your models here.
class Events(models.Model):
    db_table = "Events"
    eventName = models.CharField(max_length=30)
