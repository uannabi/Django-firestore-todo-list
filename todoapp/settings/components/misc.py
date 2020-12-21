from decouple import config, Csv
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy



AdminSite.site_title = ugettext_lazy('ToDo Admin')
AdminSite.site_header = ugettext_lazy('ToDo Administration')
AdminSite.index_title = ugettext_lazy('ToDo ADMINISTRATION')


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROOT_URLCONF = 'todoapp.urls'
WSGI_APPLICATION = 'todoapp.wsgi.application'
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost, 127.0.0.1', cast=Csv())
INTERNAL_IPS = config('INTERNAL_IPS', default='127.0.0.1', cast=Csv())
