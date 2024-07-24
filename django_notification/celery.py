from celery import Celery
from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_notification.settings')

app = Celery('django_notification')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_routes = {
    'newapp.tasks.task1': {
        'queue': 'queue1'
    },
    'newapp.tasks.task2': {
        'queue': 'queue2'
    }
}
app.autodiscover_tasks()
