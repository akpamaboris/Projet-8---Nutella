web: python manage.py runserver 
web: python manage.py makemigrations
web: python manage.py migrate
web: gunicorn mysite.wsgi:application --log-file - --log-level debug
