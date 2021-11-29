from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('', views.index, name='index'),
    url('location/<int:location_id>/', views.location, name='location'),
    url('category/<int:category_id>/', views.category, name='category'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^images',views.images,name ='images')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
