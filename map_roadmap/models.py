from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Trips(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    trip_json = models.JSONField()

    def __str__(self):
        return f"{self.username}"