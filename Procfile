release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
web: gunicorn Novost_BackEnd.wsgi --log-file -