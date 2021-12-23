# vcoder

# 1> git clone https://github.com/manhkhuat83/vcoder.git
# 2> pip install -r requirements.txt
# 3> python manage.py migrate
# 4> python manage.py runserver
# config db for sqlite3 in core/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
