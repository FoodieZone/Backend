import random
import requests
from .secrets import KAKAO_MAP_REST_API_KEY

def check_category_available(word):
    available = {'한정식', '술집', '햄버거', '중식', '샐러드', '국수', '떡볶이', '중국요리',
                 '일식', '삼겹살', '순대', '장어', '피자', '곱창,막창', '갈비', '양식',
                 '떡,한과', '베트남음식', '닭요리', '칵테일바', '감자탕', '칼국수', '이탈리안',
                 '족발,보쌈', '초밥,롤', '분식', '양꼬치', '간식', '와인바', '국밥', '참치회',
                 '한식', '아이스크림', '샤브샤브', '치킨', '호프,요리주점', '일본식라면', '냉면',
                 '찌개,전골', '일식집', '돈까스,우동', '오리', '육류,고기', '실내포장마차',
                 '제과,베이커리', '파리바게뜨', '아구', '해물,생선', '회', '일본식주점'}

    bar_similar_words = {'술집', '호프,요리주점', '실내포장마차', '일본식주점'}

    if word in available:
        if word in bar_similar_words:
            word = '요리주점'
        return word
    return ''

def parse_document(response):
    food_set = set()
    for document in response['documents']:
        food_category = list(map(lambda x: x.strip(), document['category_name'].split(">")))
        if len(food_category) >= 3:
            food_name = food_category[2]
            if check_category_available(food_name):
                food_set.add(food_name)
        elif len(food_category) == 2:
            food_name = food_category[1]
            if check_category_available(food_name):
                food_set.add(food_name)
        else:
            continue
    return food_set

def get_location(start_x, start_y, end_x, end_y, depth):
    food_round_set = set()
    page_num = 1
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    params = {'query': "음식점",
              'page': page_num,
              'rect': f'{start_x},{start_y},{end_x},{end_y}',
              'category_group_code': 'FD6'}
    headers = {"Authorization": "KakaoAK " + KAKAO_MAP_REST_API_KEY}
    response = requests.get(url, params=params, headers=headers, timeout=10).json()
    total_cnt = response['meta']['total_count']
    if depth >= 10:
        return food_round_set
    if len(food_round_set) >= 32:
        return food_round_set
    if total_cnt > 45:
        mid_x, mid_y = (start_x + end_x) / 2, (start_y + end_y) / 2
        # left down
        food_round_set.update(get_location(start_x, start_y, mid_x, mid_y, depth+1))
        # right down
        food_round_set.update(get_location(mid_x, start_y, end_x, mid_y, depth+1))
        # left up
        food_round_set.update(get_location(start_x, mid_y, mid_x, mid_y, depth+1))
        # right up
        food_round_set.update(get_location(mid_x, mid_y, end_x, end_y, depth+1))
        return food_round_set
    if response['meta']['is_end']:
        food_set = parse_document(response)
        food_round_set.update(food_set)
        return food_round_set
    page_num += 1
    food_set = parse_document(response)
    food_round_set.update(food_set)

    if len(food_round_set) >= 32:
        return food_round_set


    return food_round_set

def get_food_image(food_name):
    # food_name = 'image' # dummy data
    food_image_dict = {'햄버거': 'image', '피자': 'image', '족발,보쌈': 'image', '오리': 'image',
                       '칵테일바': 'image', '술집': 'image', '샤브샤브': 'image', '돈까스,우동': 'image',
                       '감자탕': 'image', '떡,한과': 'image', '양식': 'image', '떡볶이': 'image',
                       '일본식주점': 'image', '간식': 'image', '아이스크림': 'image', '삼겹살': 'image',
                       '육류,고기': 'image', '제과,베이커리': 'image', '와인바': 'image', '칼국수': 'image',
                       '치킨': 'image', '한식': 'image', '한정식': 'image', '참치회': 'image',
                       '호프,요리주점': 'image', '파리바게뜨': 'image', '분식': 'image', '곱창,막창': 'image',
                       '국수': 'image', '일식': 'image', '양꼬치': 'image', '샐러드': 'image',
                       '실내포장마차': 'image', '찌개,전골': 'image', '순대': 'image', '갈비': 'image',
                       '일식집': 'image', '중국요리': 'image', '장어': 'image', '해물,생선': 'image',
                       '냉면': 'image', '닭요리': 'image', '중식': 'image', '초밥,롤': 'image',
                       '아구': 'image', '베트남음식': 'image', '일본식라면': 'image', '국밥': 'image',
                       '이탈리안': 'image', '회': 'image'}
    hostname = 'localhost:8000'
    image_path = hostname+'/static/'+food_image_dict[food_name]+".png"
    return image_path

def match_food_and_image(food_round):
    result = []
    for food in food_round:
        result.append({'image': get_food_image(food),
                       'name': food})
    return result

def get_round_info(lng, lat):
    start_x, start_y = float(lng), float(lat)
    # 위도 100m 는 약 0.45 (latitude) y
    # 경도 100m 는 약 0.0009 (longitude) x
    next_x, next_y = 0.0009, 0.45

    result = list(get_location(start_x, start_y, start_x+next_x, start_y+next_y, depth=0))
    if len(result) >= 32: # 16 강
        sample_result = random.sample(result, 32)
        return match_food_and_image(sample_result)
    if 16 <= len(result) < 32: # 8 강
        sample_result = random.sample(result, 16)
        return match_food_and_image(sample_result)
    return []
