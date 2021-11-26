from django.contrib import admin
from .models import photos, Location, Category

# Register your models here.

admin.site.register(photos)
admin.site.register(Location)
admin.site.register(Category)
