DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'anawesomesecretkeythatisasecretmakeit50charsorso!!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbtable',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': '', 
        'PORT': '',
    },
}

COMPRESS_AUTO = False