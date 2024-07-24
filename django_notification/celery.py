from celery import Celery, chain, group
from os import environ

from newapp.tasks import task, task1, task2, task3

environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_notification.settings')

app = Celery('django_notification')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.task_routes = {
#     'newapp.tasks.task1': {
#         'queue': 'queue1'
#     },
#     'newapp.tasks.task2': {
#         'queue': 'queue2'
#     }
# }
app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority'
}
task_group = group(task1.s(), task2.s(), task3.s())
task_chain = chain(task.s(), task1.s(), task2.s(), task3.s())

app.autodiscover_tasks()
