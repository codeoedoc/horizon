# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import socket

from django.utils.translation import ugettext_lazy as _

socket.setdefaulttimeout(1)

LOGIN_URL = '/auth/login/'
LOGOUT_URL = '/auth/logout/'
LOGIN_REDIRECT_URL = '/'

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TESTSERVER = 'http://testserver'

USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django_nose',
    'horizon',
    'horizon.tests',
    'horizon.dashboards.nova',
    'horizon.dashboards.syspanel',
    'horizon.dashboards.settings',
    'horizon.tests.test_dashboards.cats',
    'horizon.tests.test_dashboards.dogs'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'horizon.middleware.HorizonMiddleware')

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'horizon.context_processors.horizon')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'horizon.loaders.TemplateLoader'
)

STATIC_URL = '/static/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

ROOT_URLCONF = 'horizon.tests.testurls'
TEMPLATE_DIRS = (os.path.join(ROOT_PATH, 'tests', 'templates'))
SITE_ID = 1
SITE_BRANDING = 'OpenStack'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--nocapture',
             '--nologcapture',
             '--exclude-dir=horizon/conf/',
             '--cover-package=horizon',
             '--cover-inclusive']

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = False

HORIZON_CONFIG = {
    'dashboards': ('nova', 'syspanel', 'settings'),
    'default_dashboard': 'nova',
    "password_validator": {
        "regex": '^.{8,18}$',
        "help_text": _("Password must be between 8 and 18 characters.")
    },
    'user_home': None
}

AVAILABLE_REGIONS = [
    ('http://localhost:5000/v2.0', 'local'),
    ('http://remote:5000/v2.0', 'remote'),
]

OPENSTACK_KEYSTONE_URL = "http://localhost:5000/v2.0"
OPENSTACK_KEYSTONE_DEFAULT_ROLE = "Member"

OPENSTACK_KEYSTONE_BACKEND = {
    'name': 'native',
    'can_edit_user': True
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'test': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
        },
        'horizon': {
            'handlers': ['test'],
            'propagate': False,
        },
        'novaclient': {
            'handlers': ['test'],
            'propagate': False,
        },
        'keystoneclient': {
            'handlers': ['test'],
            'propagate': False,
        },
        'glanceclient': {
            'handlers': ['test'],
            'propagate': False,
        },
        'quantum': {
            'handlers': ['test'],
            'propagate': False,
        },
        'nose.plugins.manager': {
            'handlers': ['null'],
            'propagate': False,
        }
    }
}
