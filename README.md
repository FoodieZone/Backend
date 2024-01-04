## :: Getting Started

### 1. Deploy with Docker Image 🐳

```
$ docker run -d -p 8080:8080 freemjstudio/foodie-django
```

- [Docker Hub](https://hub.docker.com/r/freemjstudio/foodie-django)

### 2. Deploy with Git Repository 🐱

First clone the repository from Github and switch to the new directory:

```
$ git clone git@github.com/USERNAME/{{ project_name }}.git
$ cd {{ project_name }}
```

Activate the virtualenv for your project.

Install project dependencies:

```
$ pip install -r requirements.txt
```

Then simply apply the migrations:

```
$ python manage.py migrate
```

You can now run the development server:

```
$ python manage.py runserver
```


       
## :: Foodie Backend APIs 💻

1. rounds API 
- get food category and image for 8 or 16 rounds
- if there's no enough data, the API returns 0

| request | example                                                      |
|---------|--------------------------------------------------------------|
 | GET    | http://{SERVER_IP}:8000/restaurants/rounds/?lng=127.0363&lat=37.5003  |

 - Example Response
```json
{
   "round":32,
   "is_self_category":false,
   "foods":[
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"제과,베이커리"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"칵테일바"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"초밥,롤"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"떡볶이"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"치킨"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"중국요리"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"일본식주점"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"샐러드"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"육류,고기"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"이탈리안"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"국밥"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"와인바"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"떡,한과"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"중식"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"실내포장마차"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"피자"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"감자탕"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"술집"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"일식"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"양식"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"해물,생선"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"한정식"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"햄버거"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"순대"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"한식"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"돈까스,우동"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"냉면"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"찌개,전골"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"호프,요리주점"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"국수"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"일식집"
      },
      {
         "image":"http://127.0.0.1:8000/static/image.png",
         "name":"양꼬치"
      }
   ]
}
```

2.results API

|request| example                                                               |
|-------|-----------------------------------------------------------------------|
| GET  | http://{SERVER_IP}:8000/restaurants/results/?lng=127.0363&lat=37.5003&name=햄버거 |

- Example Response

```json
{
   "restaurants":[
      {
         "lng":127.0358379250339,
         "lat":37.499633048878934,
         "image":"http://127.0.0.1:8000/static/image.png",
         "icon":"http://127.0.0.1:8000/static/image.png",
         "address":"서울 강남구 역삼동 736-55",
         "name":"바스버거 역삼점",
         "food_name":"햄버거",
         "distance":84.0,
         "kakao_maps_id":"218274780"
      },
      {
         "lng":127.02568305264,
         "lat":37.5011674033572,
         "image":"http://127.0.0.1:8000/static/image.png",
         "icon":"http://127.0.0.1:8000/static/image.png",
         "address":"서울 서초구 서초동 1305-5",
         "name":"파이브가이즈 강남",
         "food_name":"햄버거",
         "distance":943.0,
         "kakao_maps_id":"1725176424"
      },
      {
         "lng":127.03241956181776,
         "lat":37.49775543833608,
         "image":"http://127.0.0.1:8000/static/image.png",
         "icon":"http://127.0.0.1:8000/static/image.png",
         "address":"서울 강남구 역삼동 823-16",
         "name":"데일리픽스",
         "food_name":"햄버거",
         "distance":444.0,
         "kakao_maps_id":"717158192"
      },
      {
         "lng":127.029332806632,
         "lat":37.4932485081661,
         "image":"http://127.0.0.1:8000/static/image.png",
         "icon":"http://127.0.0.1:8000/static/image.png",
         "address":"서울 서초구 서초동 1329-8",
         "name":"파파이스 강남점",
         "food_name":"햄버거",
         "distance":996.0,
         "kakao_maps_id":"772414643"
      },
      {
         "lng":127.034379691839,
         "lat":37.5009759812561,
         "image":"http://127.0.0.1:8000/static/image.png",
         "icon":"http://127.0.0.1:8000/static/image.png",
         "address":"서울 강남구 역삼동 644-5",
         "name":"스매쉬치즈버거",
         "food_name":"햄버거",
         "distance":185.0,
         "kakao_maps_id":"431631970"
      },
      {
         "lng":127.0317430144742,
         "lat":37.49706635210059,
         "image":"http://127.0.0.1:8000/static/image.png",
         "icon":"http://127.0.0.1:8000/static/image.png",
         "address":"서울 강남구 역삼동 827-49",
         "name":"크라이치즈버거 강남점",
         "food_name":"햄버거",
         "distance":539.0,
         "kakao_maps_id":"1227343872"
      },
      {
         "lng":127.02857422109,
         "lat":37.4996503462515,
         "image":"http://127.0.0.1:8000/static/image.png",
         "icon":"http://127.0.0.1:8000/static/image.png",
         "address":"서울 강남구 역삼동 818-11",
         "name":"칙바이칙 강남역점",
         "food_name":"햄버거",
         "distance":687.0,
         "kakao_maps_id":"649575231"
      },
      {
         "lng":127.024455630304,
         "lat":37.5034670305094,
         "image":"http://127.0.0.1:8000/static/image.png",
         "icon":"http://127.0.0.1:8000/static/image.png",
         "address":"서울 서초구 서초동 1303-31",
         "name":"슈퍼두퍼 강남점",
         "food_name":"햄버거",
         "distance":1104.0,
         "kakao_maps_id":"720883151"
      }
   ]
}
```

3. static images API 

|request| example                        |
|-------|--------------------------------|
| GET  | http://{SERVER_IP}:8000/static/image.png |
