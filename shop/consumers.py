import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Product
from asgiref.sync import sync_to_async
from channels.layers import BaseChannelLayer

class ProductConsumer(AsyncWebsocketConsumer):
    channel_layer: BaseChannelLayer  # <-- аннотация для Pylance

    async def connect(self):
        await self.channel_layer.group_add("products_group", self.channel_name)
        await self.accept()
        await self.send_count()

    async def disconnect(self, code):  # <-- параметр называется 'code'
        await self.channel_layer.group_discard("products_group", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        await self.send_count()

    @sync_to_async
    def get_count(self):
        return Product.objects.count()

    async def send_count(self):
        count = await self.get_count()
        await self.send(text_data=json.dumps({'count': count}))

    async def product_update(self, event):
        await self.send_count()
