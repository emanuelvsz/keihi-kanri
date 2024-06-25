#!/bin/bash

python manage.py migrate
python manage.py loaddata month.json year.json
python manage.py runserver 0.0.0.0:8000