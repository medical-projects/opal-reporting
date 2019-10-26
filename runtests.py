"""
Standalone test runner for reporting plugin
"""
import sys
from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    DATE_FORMAT= 'd/m/Y',
    DATE_INPUT_FORMATS = ['%d/%m/%Y'],
    DATETIME_FORMAT = 'd/m/Y H:i:s',
    DATETIME_INPUT_FORMATS = ['%d/%m/%Y %H:%M:%S'],
    ROOT_URLCONF='opal.urls',
    STATIC_URL='/assets/',
    COMPRESS_ROOT='/tmp/',
    OPAL_BRAND_NAME="reporting",
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.request',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                    'opal.context_processors.settings',
                    'opal.context_processors.models'
                ],
                # ... some options here ...
            },
        },
    ],
    MIDDLEWARE=(
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'opal.middleware.AngularCSRFRename',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'opal.middleware.DjangoReversionWorkaround',
        'reversion.middleware.RevisionMiddleware'
    ),
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'axes',
        'compressor',
        'opal',
        'reporting',
        'reporting.tests',
    )
)

import django
django.setup()

from opal.core import application

class Application(application.OpalApplication):
    pass


from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
if len(sys.argv) == 2:
    failures = test_runner.run_tests([sys.argv[-1], ])
else:
    failures = test_runner.run_tests(['reporting', ])
if failures:
    sys.exit(failures)
