from channels.consumer import SyncConsumer , AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class my_consumer(AsyncConsumer):
    print("dasdas")