# -*- coding: utf-8 -*-
"""

Django settings for development environment

"""
from base import *  # noqa

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
		'NAME': '3mw',
        'USER': '3mwuser',
        'PASSWORD': '3mwuser@123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
		'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
