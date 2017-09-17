# Geo Django Playground

## Setup

```
$ vagrant up
$ vagrant ssh
```

```
$ cd /vagrant
$ direnv allow .
$ echo 'create database if not exists mysite' | mysql -uroot -p
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

Access to [http://192.168.33.10/admin](http://192.168.33.10/admin) in your browser.
