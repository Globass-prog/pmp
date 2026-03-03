from .base import *

import os

DEBUG = False

ALLOWED_HOSTS = ['*']  # temporaire pour test

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# =========================
# DEVELOPMENT SETTINGS
# =========================

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# =========================
# DATABASE (SQLite)
# =========================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# =========================
# EMAIL (Console for Dev)
# =========================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# =========================
# CORS (Allow Frontend)
# =========================

CORS_ALLOW_ALL_ORIGINS = True


# =========================
# STATIC & MEDIA
# =========================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# =========================
# TEMPLATES (Dashboard Support)
# =========================

TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]


# =========================
# REST FRAMEWORK (JWT)
# =========================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}


# =========================
# JAZZMIN ADMIN BRANDING
# =========================

JAZZMIN_SETTINGS = {
    "site_title": "Project Manager",
    "site_header": "Project Manager Admin",
    "site_brand": "PM SaaS",
    "welcome_sign": "Bienvenue sur ton Dashboard",
    "copyright": "PM 2026",

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "users.User": "fas fa-user",
        "projects.Project": "fas fa-folder",
        "tasks.Task": "fas fa-tasks",
        "comments.Comment": "fas fa-comments",
    },

    "topmenu_links": [
        {"name": "Dashboard", "url": "/admin/dashboard/"},
        {"model": "projects.Project"},
        {"model": "tasks.Task"},
    ],
}