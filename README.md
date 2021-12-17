# vcoder
1> git clone https://github.com/h4cktivist/devSearch.git
2> pip install -r requirements.txt
3> cd core/settings:
   -change database settings
     DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
    }
4> python manage.py migrate
5> python manage.py runserver
