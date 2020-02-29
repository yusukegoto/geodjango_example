# Geo Django Playground

- [geodjango database api 1.11](https://docs.djangoproject.com/en/1.11/ref/contrib/gis/db-api/#compatibility-tables)
- [geodjango required libraries 1.11](https://docs.djangoproject.com/en/1.11/ref/contrib/gis/install/geolibs/)

## Setup

```
$ docker-compose build
$ docker-compose up -d db
```

```
$ docker-compose run --rm app bash
(geo) pipenv shell
(geo): ./manage.py migrate
(geo): ./manage.py createsupersuser
(geo): ./manage.py runserver 0.0.0.0:8000
```

Access to [http://192.168.33.10:8000/admin](http://192.168.33.10:8000/admin) in your browser.


## Behavior

`./manage.py list_nearest_branch` shows an example of geodjango with mysql usage.
