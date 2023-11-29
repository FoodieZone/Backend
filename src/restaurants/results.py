import requests
from .secrets import KAKAO_MAP_REST_API_KEY
import time
from bs4 import BeautifulSoup as bs

def get_restaurants_info(lng, lat, name):
    restaurants = []
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    image_search_url = "https://search.naver.com/search.naver"
    
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
        kakao_maps_id = place_url.split('/')[-1]
        food_category = list(map(lambda x:x.strip(), document['category_name'].split(">")))
        try:
            image_search_parmas = {"query":place_name}
            image_search_response = requests.get(image_search_url, params=image_search_parmas, timeout=10)
            soup = bs(image_search_response.text, 'lxml')
            image_tag = soup.select('div.rec_thumb > img.img')[0]
            image = image_tag.get("src")
            time.sleep(0.1)
        except:
            image = "http://127.0.0.1:8000/static/image.png"
        if name not in food_category:
            continue
        if len(food_category) >= 3:
            food_name = food_category[2]
        else:
            food_name = food_category[-1]
        distance = float(document['distance'])
        restaurant = {"lng":lng,
                      "lat":lat,
                      "image":image,
                      "address":address,
                      "name": place_name,
                      "food_name":food_name,
                      "distance":distance,
                      "kakao_maps_id":kakao_maps_id}
        restaurants.append(restaurant)
    return restaurants
