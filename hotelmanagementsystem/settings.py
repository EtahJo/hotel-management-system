"""
Django settings for hotelmanagementsystem project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@7!@0z9ncy3q2gd915e39e-f$4s441#v(4p!mr%kdl5i#ln_$^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hotel',
    'userauth',
    'addon',
    'user_dashboard',

    # 'import-export',
    # 'django-crispy-forms',
    # 'django-mathfilters',
    # 'django-taggit',
    # 'django-ckeditor-5'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hotelmanagementsystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hotelmanagementsystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL= "userauth.User"

JAZZMIN_SETTINGS = {
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Santa",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Your #1 marketplace for collectibles",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "/images/logo.png",
  

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Santa Hotel, Login Now",

    # Copyright on the footer
    "copyright": "All Right Reserved 2023",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["auth.User", "auth.Group"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name":"Company","url":"/admin/addons/company"},
        {"name":"Users","url":"/admin/userauths/user/"},

        {"model":"AUTH_USER_MODEL.User"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

 

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        "hotel", 
        "hotel.Hotel", 
        "hotel.Room", 
        "hotel.Booking"
        "hotel.BookingDetails",
        "hotel.Guest",
        "hotel.RoomServices",
        "userauths",
        "addons"
        ],

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "books": [{
    #         "name": "Make Messages", 
    #         "url": "make_messages", 
    #         "icon": "fas fa-comments",
    #         "permissions": ["books.view_book"]
    #     }]
    # },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "admin.LogEntry":"fas fa-file",
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",

        "userauth.User":"fas fa-user",
        "userauth.Profile":"fas fa-address-card",

        "hotel.Hotel":"fas fa-th",
        "hotel.Booking":"fas fa-calendar-week",
        "hotel.BookingDetail":"fas fa-calendar-alt",
        "hotel.Guest":"fas fa-user",
        "hotel.Room":"fas fa-bed",
        "hotel.RoomServices":"fas fa-user-cog",
        "hotel.Notification":"fas fa-bell",
        "hotel.Coupon":"fas fa-tag",
        "hotel.Bookmark":"fas fa-heart"
    },
  
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},

}


JAZZMIN_UI_TWEAKS = {
   "navbar_small_text":False,
   "footer_small_text":False,
   "body_small_text":True,
   "brand_small_text":False,
   'brand_colour':"navbar-indigo",
   "accent":"accent-olive",
   "navbar":"navbar-indigo navabr-dark",
   "no_navbar_border":False,
   "navbar_fixed":False,
   "layout_boxed":False,
   "footer_fixed":False,
   "sidebar_fixed":False,
   "sidebar":"sidebar-dark-indigo",
   "sidebar_nav_small_text":False,
   "sidebar_disable_expand":False,
   "sidebar_nav_child_indent":False,
   "sidebar_nav_compact_style":False,
   "sidebar_nav_legacy_style":False,
   "sidebar_nav_flat_style":False,
   "theme":"cyborg",
   "dark_mode_theme":"cyborg",
   "button_classes":{
    "primary":"btn-primary",
    "secondary":"btn-secondary",
    "info":"btn-info",
    "warning":"btn-warning",
    "danger":"btn-danger",
    "success":"btn-success"
   }
}
