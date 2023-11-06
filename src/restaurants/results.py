import requests
from .secrets import KAKAO_MAP_REST_API_KEY

def get_restaurants_info(lng, lat, name):
    restaurants = []
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"

    params = {"query": name, "category_group_code":"FD6", "x": lng, "y":lat}
    headers = {"Authorization": "KakaoAK "+KAKAO_MAP_REST_API_KEY}
    response = requests.get(url, params=params, headers=headers, timeout=10)
    response = response.json()

    for document in response['documents']:
        lng = float(document['x'])
        lat = float(document['y'])
        address = document['address_name']
        name = document['place_name']
        food_name = document['category_name'].split(">")[-1].strip()
        distance = float(document['distance'])
        restaurant = {"lng":lng,
                      "lat":lat,
                      "address":address,
                      "name": name,
                      "food_name":food_name,
                      "distance":distance}
        restaurants.append(restaurant)
    return restaurants
