from django import forms
from room.models import RoomMessage, RoomList, Room


class RoomMessageForm(forms.ModelForm):
    class Meta:
        model = RoomMessage
        fields = ['room_message', 'message_list']

class RoomListForm(forms.ModelForm):
    class Meta:
        model = RoomList
        fields = ['room']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'users']