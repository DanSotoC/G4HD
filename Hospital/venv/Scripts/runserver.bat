@echo off
call activate
cd ..
cd ..
cd hospital
python manage.py runserver 0.0.0.0:8000
exit