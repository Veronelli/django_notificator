from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import requests

@shared_task
def send_notification_task(message: str):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notifications',
        {
            'type': 'send_notification',
            'message': message
        }
    )