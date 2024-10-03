from django.conf import settings
from celery.schedules import crontab
from celery import Celery
import os

app = Celery('prueba_all_meal')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Set DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'prueba_all_meal.settings'

# Initialize Django
import django
django.setup()

app.conf.beat_schedule = {
    'send-message': {
        'task': 'my_app.send_message_to_slack',
        'schedule': crontab(minute='*/1'),
        'args': ('Hello from Celery!',),
    },
}