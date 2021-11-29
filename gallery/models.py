from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def save_catego(self):
        self.save()

    def update_catego(self, name):
        self.name = name
        self.save()

    def delete_catego(self):
        self.delete()

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def save_loc(self):
        self.save()

    def update_loc(self, name):
        self.name = name
        self.save()

    def delete_loc(self):
        self.delete()

    def __str__(self):
        return self.name

class photos(models.Model):
    pic_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    phone_number = models.CharField(max_length = 10,blank =True)

    def save_photos(self):
        self.save()

    def update_photos(self, pic_name, description, location, category):
        self.pic_name = pic_name
        self.description = description
        self.location = location
        self.category = category
        self.save()



    #search photos
    @classmethod
    def search_photos(cls,search_term):
        photos_by_category = cls.filter_by_category(search_term)
        photos_by_location = cls.filter_by_location(search_term)
        return photos_by_category.union(photos_by_location)
    
    @classmethod
    def get_all_photos(cls):
        Photos =photos.objects.all()
        return Photos
    
    @classmethod
    def get_photos_by_id(cls, id):
        Photos =photos.objects.get(id=id)
        return Photos
    
    @classmethod
    def filter_by_location(cls, location):
        Photos =photos.objects.filter(location_name = location)
        return Photos
    
    @classmethod
    def filter_by_category(cls, category):
        Photos =photos.objects.filter(category_name = category)
        return Photos
    
    def delete_photos(self):
        self.delete()

    def __str__(self):
        return self.pic_name



