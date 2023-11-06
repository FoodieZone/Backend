import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from .results import get_restaurants_info

def index(request):
    return HttpResponse("this is restaurant app")

def results(request):
    context = {}
    lng = request.GET.get('lng') # 경도 x float
    lat = request.GET.get('lat') # 위도 y float
    name = request.GET.get('name') # str
    restaurants = get_restaurants_info(lng, lat, name)
    context['restaurants'] = restaurants
    context = json.dumps(context, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(context)
