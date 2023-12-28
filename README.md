## :: Getting Started

### 1. Deploy with Docker Image 🐳

```
$ docker run -d -p 8080:8080 freemjstudio/foodie-django
```

- https://hub.docker.com/repository/docker/freemjstudio/foodie-django/general

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

2.results API

|request| example                                                               |
|-------|-----------------------------------------------------------------------|
| GET  | http://{SERVER_IP}:8000/restaurants/results/?lng=127.0363&lat=37.5003&name=햄버거 |

3. static images API 

|request| example                        |
|-------|--------------------------------|
| GET  | http://{SERVER_IP}:8000/static/image.png |
