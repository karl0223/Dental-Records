import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dentalclinic.settings')         # django module environment variable - path of the settings

celery = Celery('dentalclinic')
celery.config_from_object('django.conf:settings', namespace='CELERY')               # go to django conf and load the settings
celery.autodiscover_tasks()