import json
import requests
from .secrets import *

def getRestaurantList(lng, lat, name):
    restaurantItems = []
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    '''
        KAKAO MAP API parameters 
        longitude : x, 경도 
        latitude : y, 위도 
    '''
    params = {"query": name, "category_group_code":"FD6", "x": lng, "y":lat}
    headers = {"Authorization": "KakaoAK "+KAKAO_MAP_REST_API_KEY}
    response = requests.get(url, params=params, headers=headers).json()

    '''
        lng: float / 경도 / not null / 127.xxx
        lat: float / 위도 / not null / 37.xxx
        image: str / 대표 이미지 / nullable / "http://"
        address: str / 주소 / not null / "서울시 동작구"
        name: str / 식당 이름 / not null / "버거운버거"
        food_name: str / 대표 음식 이름 / not null / "햄버거"
        distance: float / 거리 (m 단위) / not null / 223.xx
    '''

    for document in response['documents']:
        lng = float(document['x'])
        lat = float(document['y'])
        address = document['address_name']
        name = document['place_name']
        food_name = document['category_name'].split(">")[-1].strip()
        distance = float(document['distance'])
        restaurant = {"lng":lng, "lat":lat, "address":address, "name": name, "food_name":food_name, "distance":distance}
        restaurantItems.append(restaurant)
    return restaurantItems