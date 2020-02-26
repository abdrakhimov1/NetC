from django.db import models

class Room(models.Model):

    name = models.TextField(max_length=64)
    users = models.ForeignKey(to='users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комната'

class RoomList(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Список сообщений комнаты'
        verbose_name_plural = 'Списки сообщений комнаты'

class RoomMessage(models.Model):

    room_message = models.TextField(max_length=256)
    message_list = models.ForeignKey(RoomList, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сообщение комнаты'
        verbose_name_plural = 'Сообщения комнаты'




