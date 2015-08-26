from .base import *  # NOQA

# Django Debug Toolbar
INSTALLED_APPS += (
    'debug_toolbar',
)
# Django Debug Panel Middleware
MIDDLEWARE_CLASSES += (
    'debug_toolbar.base.',
)
