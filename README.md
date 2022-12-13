# zakzk
Zkteco api using [`pzyk`](https://github.com/fananimi/pyzk) and [`django-rest-framework`](https://github.com/encode/django-rest-framework).

## Setup
#### Python3
##### Init
```
pip install -r requirements.txt && python manage.py makemigrations && python migrate
```
##### Serve
```
python manage.py runserver --insecure 0.0.0.0:8000
```
#### Docker
```
docker compose up -d
```
