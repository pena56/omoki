from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories')
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.event_name