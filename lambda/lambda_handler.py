"""
AWS Lambda entry point.

Mangum translates API Gateway / ALB events into WSGI requests
and returns the Django response as a Lambda-compatible dict.
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imagesite.settings")

import django  # noqa: E402
django.setup()

from mangum import Mangum  # noqa: E402
from imagesite.wsgi import application  # noqa: E402

handler = Mangum(application, lifespan="off")
