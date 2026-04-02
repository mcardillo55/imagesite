"""
AWS Lambda entry point using apig_wsgi to bridge API Gateway to Django WSGI.
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imagesite.settings")

import django  # noqa: E402
django.setup()

from apig_wsgi import make_lambda_handler  # noqa: E402
from imagesite.wsgi import application  # noqa: E402

prefix = os.environ.get("SCRIPT_NAME", "").rstrip("/")

if prefix:
    class StripPrefix:
        def __init__(self, wsgi_app, prefix):
            self.wsgi_app = wsgi_app
            self.prefix = prefix

        def __call__(self, environ, start_response):
            path = environ.get("PATH_INFO", "")
            if path.startswith(self.prefix):
                environ["PATH_INFO"] = path[len(self.prefix):] or "/"
                environ["SCRIPT_NAME"] = self.prefix
            return self.wsgi_app(environ, start_response)

    handler = make_lambda_handler(StripPrefix(application, prefix))
else:
    handler = make_lambda_handler(application)
