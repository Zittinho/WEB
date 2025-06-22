from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

@receiver(post_save, sender=Product)
def notify_product_change(sender, instance, **kwargs):
    layer = get_channel_layer()
    if layer is not None:
        async_to_sync(layer.group_send)(
            'products_group',
            {
                'type': 'product_update',
                'message': 'updated',
            }
        )
