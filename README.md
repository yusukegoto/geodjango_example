# Geo Django Playground

- [geodjango database api 2.2](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/db-api/#compatibility-tables)
- [geodjango required libraries 2.2](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/install/geolibs/)

## Setup

```
$ docker-compose build
$ docker-compose up -d db
```

```
$ docker-compose run --rm app bash
> ./manage.py migrate
> ./manage.py createsupersuser
> ./manage.py runserver 0.0.0.0:8000
```

Access to [http://192.168.33.10:8000/admin](http://192.168.33.10:8000/admin) in your browser.


## Behavior

`./manage.py list_nearest_branch` shows an example of geodjango with mysql usage.
