from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length = 60)

    # objects = QuerySetManager()

    def __str__(self):
        return self.name