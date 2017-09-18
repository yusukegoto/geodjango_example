# Geo Django Playground

## Setup

```
$ vagrant up
$ vagrant ssh
```

```
$ cd /vagrant
$ direnv allow .
$ echo 'create database if not exists mysite default character set utf8' | mysql -uroot -p
$ mkdir ~/.virtualenvs
$ virtualenv ~/.virtualenvs/geo
$ . ~/.virtualenvs/geo/bin/activate
```

```
(geo): pip install -r requirements.txt
(geo): ./manage.py migrate
(geo): ./manage.py createsupersuser
(geo): ./manage.py runserver 0.0.0.0:8000
```

Access to [http://192.168.33.10:8000/admin](http://192.168.33.10:8000/admin) in your browser.


## Behavior

`./manage.py list_nearest_branch` shows an example of geodjango with mysql usage.
