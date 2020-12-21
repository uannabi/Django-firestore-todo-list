import os
from decouple import config
from todoapp.settings.paths import BASE_DIR


FIRESTORE = config('FIRESTORE', cast=bool, default=False)

if FIRESTORE:
    DATABASES = {
        'default': {
            'FIREBASE_ORM_CERTIFICATE': config('KEY_PATH', cast=str),
            'FIREBASE_ORM_BUCKET_NAME': config('BUCKET_NAME',cast=str),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
