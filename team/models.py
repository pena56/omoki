from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import cloudinary
from django.urls import reverse

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    profile_image = CloudinaryField('profile')
    about = models.TextField()
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Team)
def category_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)

    
