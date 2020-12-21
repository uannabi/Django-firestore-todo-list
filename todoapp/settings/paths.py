import os


STATIC_URL = '/static/'

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, 'api/fixtures/'),
)


BASE_DIR = os.path.dirname(PROJECT_DIR)

