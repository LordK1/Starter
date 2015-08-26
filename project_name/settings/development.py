from .base import *  # NOQA

"""
 Note: When you are developing on {{ project_name }} should use this settings on manage.py
"""
# Django Debug Toolbar
INSTALLED_APPS += (
    'debug_toolbar',
)
# Django Debug Panel Middleware
MIDDLEWARE_CLASSES += (
    'debug_toolbar.base.',
)
