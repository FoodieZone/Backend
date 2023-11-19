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
        place_name = document['place_name']
        place_url = document['place_url']
        print(place_url)
        food_category = list(map(lambda x:x.strip(), document['category_name'].split(">")))

        if name not in food_category:
            continue

        distance = float(document['distance'])
        restaurant = {"lng":lng,
                      "lat":lat,
                      "address":address,
                      "name": place_name,
                      "food_name":food_name,
                      "distance":distance}
        restaurants.append(restaurant)
    return restaurants
