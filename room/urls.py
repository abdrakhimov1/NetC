from django.urls import path
from django.urls import include

from room.views import index, get_rooms_list, room_lists_list, messages_in_list, get_everything, create_room

urlpatterns = [
    path('index', index, name='index'),
    path('get_rooms_list', get_rooms_list, name='get_room_list'),
    path('room_lists_list', room_lists_list, name='room_lists_list'),
    path('messages_in_list', messages_in_list, name='messages_in_list'),
    path('get_everything', get_everything, name='get_everything'),
    path('create_room', create_room, name='create_room')
]
