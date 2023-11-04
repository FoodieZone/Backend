from django.shortcuts import render
from django.http import HttpResponse
from .results import getRestaurantList
from django.core.serializers.json import DjangoJSONEncoder
import json
# Create your views here.

def index(request):
    return HttpResponse("this is restaurant app")

def results(request):
    context = {}
    lng = request.GET.get('lng') # 경도 x float
    lat = request.GET.get('lat') # 위도 y float
    name = request.GET.get('name') # str
    restaurantItems = getRestaurantList(lng, lat, name)
    context['restaurants'] = restaurantItems
    context = json.dumps(context, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(context)