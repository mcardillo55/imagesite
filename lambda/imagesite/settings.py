"""
Django settings for imagesite project — Lambda / read-only edition.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "f*#h^8-s_sn*p^(w&(-#e^18$a8@!8&&_^p!k9-2kc^1%i$@@8",
)

DEBUG = os.environ.get("DEBUG", "0") == "1"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# The base URL where images are served from (CloudFront / S3).
# Example: https://d1234abcde.cloudfront.net/imgsite/img
# The trailing slash is added in the template tag, so omit it here.
IMAGE_BASE_URL = os.environ.get("IMAGE_BASE_URL", "/imgsite/img")

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "images",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
]

ROOT_URLCONF = "imagesite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "imagesite.wsgi.application"

# ---------- Database (read-only SQLite) ----------
# In Lambda the package is extracted to /var/task.
# We ship db.sqlite3 inside the zip.
_DB_PATH = os.environ.get(
    "DB_PATH",
    os.path.join(BASE_DIR, "db.sqlite3"),
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # file:<path>?mode=ro opens the database read-only at the SQLite level.
        "NAME": f"file:{_DB_PATH}?mode=ro",
        "OPTIONS": {
            "uri": True,
        },
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = False
USE_TZ = True
APPEND_SLASH = True

# Static files — served from CloudFront in production.
STATIC_URL = os.environ.get("STATIC_URL", "/imgsite/static/")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
