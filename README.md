# vcoder
1> git clone https://github.com/h4cktivist/devSearch.git
<br>
2> pip install -r requirements.txt
<br>
3> cd core/settings:
   <br>
     DATABASES = {
     <br>
      'default': {
      <br>
          'ENGINE': 'django.db.backends.sqlite3',
          <br>
          'NAME': BASE_DIR / 'db.sqlite3',
          <br>
      }
      <br>
    }
    <br>
4> python manage.py migrate
<br>
5> python manage.py runserver
