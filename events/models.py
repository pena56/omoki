from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import cloudinary
from django.urls import reverse

from category.models import Category

# Create your models here.
class Event(models.Model):
    FEATURED_CHOICE = (
        ('featured', 'Featured'),
        ('not_featured', 'Not Featured'), 
    )


    event_title = models.CharField(max_length=200)
    event_location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    cover_image = CloudinaryField()
    image_1 = CloudinaryField(null=True, blank=True)
    image_2 = CloudinaryField(null=True, blank=True)
    image_3 = CloudinaryField(null=True, blank=True)
    image_4 = CloudinaryField(null=True, blank=True)
    event_date = models.DateTimeField(auto_now_add=True)
    featured = models.CharField(max_length=50, choices=FEATURED_CHOICE, default='not_featured')

    def __str__(self):
        return self.event_title

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])


@receiver(pre_delete, sender=Event)
def category_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)


