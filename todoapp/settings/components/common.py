from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
PRODUCTION = config('PRODUCTION', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY',)