from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.

class photos(models.Model):
    pic_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
