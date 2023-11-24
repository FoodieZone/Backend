import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from .results import get_restaurants_info
from .rounds import get_round_info

def index(request):
    return HttpResponse("this is restaurant app")

def results(request):
    context = {}
    lng = request.GET.get('lng') # 경도 x float
    lat = request.GET.get('lat') # 위도 y float
    name = request.GET.get('name') # str
    restaurants = get_restaurants_info(lng=lng, lat=lat, name=name)
    context['restaurants'] = restaurants
    context = json.dumps(context, cls=DjangoJSONEncoder,ensure_ascii = False)
    return HttpResponse(context)

def rounds(request):
    context = {}
    lng = request.GET.get('lng')  # 경도 x float
    lat = request.GET.get('lat')  # 위도 y float
    is_self_category, food_round = get_round_info(lng=lng, lat=lat)
    context['round'] = len(food_round) # 8 or 16 (16, 32)
    context['is_self_category'] = is_self_category
    context['foods'] = food_round
    context = json.dumps(context, cls=DjangoJSONEncoder, ensure_ascii=False)
    return HttpResponse(context)