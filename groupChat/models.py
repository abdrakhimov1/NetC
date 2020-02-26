from django.db import models

class GroupUser(models.Model):

    name = models.TextField(max_length=64)

    class Meta:
        verbose_name = 'Групповой пользователь'
        verbose_name_plural = 'Групповые пользователи'

class GroupMessage(models.Model):
    
    content = models.TextField(max_length=256)
    owner = models.ForeignKey(to=GroupUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Групповое сообщение'
        verbose_name_plural = 'Групповые сообщения'