from django.db import models

from category.models import Category

# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    highlight_1 = models.CharField(max_length=100, null=True, blank=True)
    highlight_2 = models.CharField(max_length=100, null=True, blank=True)
    highlight_3 = models.CharField(max_length=100, null=True, blank=True)
    highlight_4 = models.CharField(max_length=100, null=True, blank=True)
    highlight_5 = models.CharField(max_length=100, null=True, blank=True)
    highlight_6 = models.CharField(max_length=100, null=True, blank=True)
    highlight_7 = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categpry')

    def __str__(self):
        return self.title
