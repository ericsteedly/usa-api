#!/bin/bash

rm db.sqlite3
rm -rf ./usaapi/migrations
python manage.py makemigrations usaapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata states
python manage.py loaddata cities
python manage.py loaddata userdetail