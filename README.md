PIZZA MIZZA
===========

Simple example of RESTful API using Django REST Framework.

### What is included

- 2 endpoints: pizzas and orders
- filter for orders (by status, customer_name)
- pagination for API results
- tests for model and API views
- 'cookpizza' management command to create few pizzas
- Admin website for manual data entrance GUI
- API docs based on builtin API documentation

### Setup & Run

#### Setup:

    git clone https://github.com/KenanBek/pizzamizza
    cd pizzamizza
    virtualenv env
    source env/bin/activate (or .\env\Scripts\activate)
    pip install -r requirements.txt

#### Run:

    cd app
    python manage.py migrate
    python manage.py test
    python manage.py createsuperuser  # if you will use /admin
    python manage.py cookpizza  # create few test pizzas, do not run twice :)
    python manage.py runserver

Check following links:

API: [http://localhost:8000/api/](http://localhost:8000/api/)

Docs: [http://localhost:8000/docs/](http://localhost:8000/docs/)

Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Project structure

I usually do not use default Django structure and change configuration of base folder for urls, settings and wsgi.
You can check my [Django Skeleton](https://github.com/KenanBek/django-skeleton) project for more info. 

    pizzamizza/
    |---app                                     # django app source folder
    |   |---pm                                  # django default conf, pm=pizza mizza
    |   |   |---settings.py
    |   |   |---urls.py
    |   |   |---wsgi.py
    |   |---pizza
    |   |   |---management
    |   |   |   |---commands/cookpizza.py       # some mokcup data for tests
    |   |   |---migrations
    |   |   |---admin.py
    |   |   |---apps.py
    |   |   |---models.py
    |   |   |---serializers.py
    |   |   |---views.py
    |   |   |---test_models.py
    |   |   |---test_views.py
    |   |---files
    |   |   |---tempaltes
    |   |---manage.py
    |   |
    |---.gitignore
    |---requirements.txt
    |---README.md
    |
