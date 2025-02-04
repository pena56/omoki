from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import cloudinary
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('category')
    description = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

@receiver(pre_delete, sender=Category)
def category_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)

    
