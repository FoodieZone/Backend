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
    bakery_similar_words = {'제과,베이커리', '파리바게뜨'}
    korean_similar_words = {'한정식', '한식'}

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

def get_location(keyword, start_x, start_y, end_x, end_y):
    food_round_set = set()
    page_num = 1

    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    params = {'query': keyword,
              'page': page_num,
              'rect': f'{start_x},{start_y},{end_x},{end_y}',
              'category_group_code': 'FD6'}
    headers = {"Authorization": "KakaoAK " + KAKAO_MAP_REST_API_KEY}

    response = requests.get(url, params=params, headers=headers, timeout=10).json()
    total_cnt = response['meta']['total_count']

    if len(food_round_set) >= 32:
        return food_round_set

    if total_cnt > 45:
        mid_x, mid_y = (start_x + end_x) / 2, (start_y + end_y) / 2
        # left down
        food_round_set.update(get_location(keyword, start_x, start_y, mid_x, mid_y))
        # right down
        food_round_set.update(get_location(keyword, mid_x, start_y, end_x, mid_y))
        # left up
        food_round_set.update(get_location(keyword, start_x, mid_y, mid_x, mid_y))
        # right up
        food_round_set.update(get_location(keyword, mid_x, mid_y, end_x, end_y))
        return food_round_set
    else:
        if response['meta']['is_end']:
            food_set = parse_document(response)
            food_round_set.update(food_set)
            return food_round_set
        else:
            page_num += 1
            food_set = parse_document(response)
            food_round_set.update(food_set)

            if len(food_round_set) >= 32:
                return food_round_set

    return food_round_set

def match_food_and_image(food_round):
    result = []
    for food in food_round:
        result.append({'image': 'image.png',
                       'name': food})
    return result

def get_round_info(lng, lat):
    categories = []
    food_round_set = set()
    start_x, start_y = float(lng), float(lat)
    # 위도 100m 는 약 0.45 (latitude) y
    # 경도 100m 는 약 0.0009 (longitude) x
    next_x, next_y = 0.0009, 0.45

    result = list(get_location("음식점", start_x, start_y, start_x+next_x, start_y+next_y))
    if len(result) >= 32: # 16 강
        return match_food_and_image(result[:32])
    elif 16 <= len(result) < 32: # 8 강
        return match_food_and_image(result[:16])
    else: # 월드컵 불가능 -> 예외처리 : 0 리턴하기
        return list([])

