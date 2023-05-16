from django.db import models


class EventsModel(models.Model):
    event_date = models.CharField(max_length=20, default="2022-02-22")
    event_name = models.CharField(max_length=128, default="NoName")
    location = models.CharField(max_length=38, default="None")
    tickets_count = models.IntegerField(default=0)
    #objects = models.Manager()
    class Meta:
        db_table = "events"
