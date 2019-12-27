from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from setups import models as s_models
from functools import reduce
# from functools import filter


class PopInfoConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'board_meeting'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        data = json.loads(data)
        cmd = data['cmd']
        if cmd == 'broadcast':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'notify_message',
                    'message': {'id': data['id']}
                }
            )

    def notify_message(self, event):
        message = event['message']
        supplier = s_models.Supplier.objects.get(pk=message['id'])
        print(supplier)
        count_all = supplier.projects.count()
        if count_all == 0:
            count_all = 1
        flt = list(filter(lambda x: x.project.status.name == 'Completed', supplier.projects.all()))
        count_completed = len(flt)

        self.send(text_data=json.dumps({
            'message': {
                'id': supplier.id,
                'name': supplier.name,
                'age': 28,
                'projects': count_all,
                'performance': 100 * count_completed / count_all
            }
        }))
