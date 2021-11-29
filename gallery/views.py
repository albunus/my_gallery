from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

from gallery.models import photos, Category, Location

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    
    if 'category' in request.GET and request.GET["category"]:
        category_id = request.GET.get("category")
        Photos = photos.objects.filter(category = category_id)

    elif 'location' in request.GET and request.GET["location"]:
        location_id = request.GET.get("location")
        Photos = photos.objects.filter(location = location_id)

    else:
        Photos = photos.objects.all()

    ctx = {'Photos':Photos, 'categories': categories, 'locations':locations }
    return render(request, 'all-gallery/index.html',ctx)


def search_results(request):

    if 'Photos' in request.GET and request.GET["Photos"]:
        search_term = request.GET.get("Photos")
        searched_Photos = photos.filter_by_location(search_term)
        message = search_term

        return render(request, 'all-gallery/search.html',{"message":message,"Photos": searched_Photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})
    
    
def image(request,Photos_id):
    try:
        Photos = photos.objects.get(id = Photos_id)
    except ValueError:
        raise Http404()
    return render(request,"all-gallery/photos.html", {"Photos":Photos})

def Photos(request, photos_id):
    locations = Location.objects.all()
    Photos = photos.objects.get(id=photos_id)
    name = Photos
    return render(request, 'photos.html', {'Photos': Photos, 'locations': locations, 'name': name})

def location(request, location_id):
    locations = Location.objects.all()
    Photos = photos.objects.filter(location_id=location_id)
    location = Location.objects.get(id=location_id)
    name = location
    return render(request, 'location.html', {'Photos': Photos, 'locations': locations, 'name':name})

def category(request, category_id):
    categories = Location.objects.all()
    Photos = photos.objects.filter(location_id=category_id)
    category = Location.objects.get(id=category_id)
    name = category
    return render(request, 'category.html', {'Photos': Photos, 'categories': categories, 'name':name})


def loc(request,location_id):
    try:
        location = Location.objects.get(id = location_id)
    except ValueError:
        raise Http404()
    return render(request,"all-gallery/index.html", {"location":location})

def cat(request,category_id):
    try:
        category = Category.objects.get(id = category_id)
    except ValueError:
        raise Http404()
    return render(request,"all-gallery/index.html", {"category":category})