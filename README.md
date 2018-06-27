https://docs.google.com/document/d/15t6xVut8JSio6IXKLGXvbB9ErU0jvCqF3Tc15dgg8ac/edit

Step to run

1. virtualenv env
2. source env/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py collectstatic --noinput
6. python manage.py createsuperuser (Create admin user credentials)
7. python manage.py runserver

Access admin page at localhost:8000/admin/