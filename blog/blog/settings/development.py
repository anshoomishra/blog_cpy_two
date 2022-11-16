from .base import *
DEBUG = True

ALLOWED_HOSTS = ["localhost"]
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

print(BASE_DIR)