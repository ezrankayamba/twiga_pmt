from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from . import models
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
            win = models.Win.objects.get(pk=data['id'])
            win.announced = True
            win.save()

    def notify_message(self, event):
        message = event['message']
        win = models.Win.objects.get(pk=message['id'])
        print(win)

        self.send(text_data=json.dumps({
            'message': {
                'id': win.id,
                'title': win.title,
                'winner': win.winner,
                'facts': list(map(lambda x: x.name, win.fact_set.all()))
            }
        }))
