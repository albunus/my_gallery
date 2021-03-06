from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

from gallery.models import Images, Category, Location

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    
    
    
    if 'category' in request.GET and request.GET["category"]:
        category_id = request.GET.get("category")
        Image = Images.objects.filter(category = category_id)
        
    elif 'location' in request.GET and request.GET["location"]:
        location_id = request.GET.get("location")
        Image = Images.objects.filter(location = location_id)
       
    else:
        Image = Images.objects.all()
            
    ctx = {'Image':Image, 'categories': categories, 'locations':locations }
    return render(request, 'all-gallery/index.html',ctx)

def search_results(request):

    title = "Category"
    locations = Location.objects.all()
    
    if 'category' in request.GET and request.GET["category"]:
        search_category=request.GET.get("category")
        searched_category = Images.search_by_category(search_category)
        message = f"{search_category}"
        
        return render(request,'all-gallery/search.html',{'message':message,'images':searched_category,'title':title,'locations':locations})
    else:
        message = "You haven't searched for any category"
        return render(request, 'all-gallery/search.html',{"message":message})
    
def get_images(request,images_id):
    try:
        images = Images.objects.get(id = images_id)
    except ValueError:
        raise Http404()
    return render(request,"all-gallery/images.html", {"images":images})

def get_location(request, location_id):
    locations = Location.objects.all()
    images = Images.objects.filter(location_id=location_id)
    location = Location.objects.get(id=location_id)
    title = location
    return render(request, 'all-gallery/search.html', {'images': images, 'locations': locations, 'title': title})

def get_category(request, category_id):
    categories = Location.objects.all()
    images = Images.objects.filter(location_id=category_id)
    category = Location.objects.get(id=category_id)
    name = category
    return render(request, 'all-gallery/search.html', {'images': images, 'categories': categories, 'name':name})


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