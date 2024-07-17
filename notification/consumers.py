import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.template import Context, Template

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        await self.accept()
        await self.channel_layer.group_add('notification', self.channel_name)
        
    async def disconnect(self, code) -> None:
        await self.channel_layer.group_discard('notification', self.channel_name)

    async def send_notification(self, event) -> None:
        message = event["message"]
        
        template = Template('<div class="notification"><p>{{message}}</p></div>')
        cnxt = Context({"message": message})
        rendered_notification = template.render(cnxt)
        
        await self.send(
            text_data=json.dumps(
                {
                    'type': 'notification',
                    'message': rendered_notification
                }
            )
        )