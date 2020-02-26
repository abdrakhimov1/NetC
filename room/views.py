from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http  import require_GET, require_POST
from room.forms import RoomMessageForm, RoomListForm, RoomForm
from django.apps import apps
import json
import ast


def index(request):
    return render(request, 'index.html')


def get_rooms_list():
    Room = apps.get_model('room', 'Room')
    
    rooms = Room.objects.all().values('id', 'name', 'users')
    return {'room_list': list(rooms)}


def room_lists_list(room_id_get):
    RoomList = apps.get_model('room', 'RoomList')
    if RoomList.objects.filter(room_id=room_id_get).exists():
        list_in_room = RoomList.objects.filter(room_id=room_id_get).values('id', 'room_id')
        # print(Message.objects.filter(chat_id=request.GET['chat_id']))
        return {'list_in_room': list(list_in_room)}



def messages_in_list(message_l_id):
    Message = apps.get_model('room', 'RoomMessage')

    if Message.objects.filter(message_list_id=message_l_id).exists():
        messages_in_list = Message.objects.filter(message_list_id=message_l_id).values('id', 'message_list_id', 'room_message')
        # print(Message.objects.filter(chat_id=request.GET['chat_id']))
        return {'messages_in_list': list(messages_in_list)}



def make_file(request):

    rooms = get_rooms_list()['room_list']

    return_dict = {}

    for each_room in rooms:
        if room_lists_list(each_room['id']):
            lists = room_lists_list(each_room['id'])['list_in_room']
            lists_dict = dict()
            for each_list in lists:
                if messages_in_list(each_list['id']):
                    positions = messages_in_list(each_list['id'])['messages_in_list']
                    positions_dict = dict()
                    for each_position in positions:

                        positions_dict['pos_' + str(each_position['id'])] = each_position['room_message']
                    
                else:

                    positions_dict = {}

                lists_dict['list_' + str(each_list['id'])] = positions_dict

        else: 

            list_dict = {}

        return_dict['room_' + str(each_room['id'])] = lists_dict
    
    return return_dict

@csrf_exempt
@require_GET
def get_everything(request):

    rooms = make_file(request)

    return JsonResponse(rooms)

@csrf_exempt
@require_POST
def create_room(request):

    Room = apps.get_model('room', 'Room')
    
    form = RoomForm(request.POST)
    
    if form.is_valid():
        
        room = form.save()
        
        return get_everything(request)
    
    return JsonResponse({'errors': form.errors}, status=400)
