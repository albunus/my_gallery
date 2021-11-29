from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('', views.index, name='index'),
    url('category/<int:category_id>/', views.get_category, name='category'),
    url(r'^search/', views.search_results, name='search_results'),
    url('location/<str:search_location>/',views.get_location,name='location'),
    url('image/<int:image_id>/',views.get_images,name='singleImage'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
