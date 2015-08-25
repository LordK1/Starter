from .base import *  # NOQA

# Django Debug Toolbar
INSTALLED_APPS += (
    'debug_toolbar',
    'debug_panel',
)
# Django Debug Panel Middleware
MIDDLEWARE_CLASSES += (
    'debug_panel.middleware.DebugPanelMiddleware',
)
