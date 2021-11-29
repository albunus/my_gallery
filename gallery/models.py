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

class Images(models.Model):
    pic_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    phone_number = models.CharField(max_length = 10,blank =True)

    def save_image(self):
        self.save()


    # update image
    def update_image(self, name, description):
        self.name = name
        self.description = description
        # self.location = location
        self.category = Category
        self.save()

    # get all images
    @classmethod
    def get_all_images(cls):
        images = Images.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(category__name__icontains=search_term)
        return pics

    @classmethod
    def filter_by_location(cls,search_location):
        location = cls.objects.filter(location__name__=search_location).all()
        return location

    def delete_image(self):
        self.delete()

    @classmethod
    def search(cls, search_term):
        images_by_category = cls.search_by_category(search_term)
        images_by_location = cls.filter_by_location(search_term)
        return images_by_category.union(images_by_location)

    def __str__(self):
        return self.name