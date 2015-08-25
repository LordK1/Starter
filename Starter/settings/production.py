__author__ = 'k1'
from .base import *

MIDDLEWARE_CLASSES += (
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)
