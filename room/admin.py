from room.models import Room, RoomMessage, RoomList
from django.contrib import admin
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    pass

class RoomMessageAdmin(admin.ModelAdmin):
    pass

class RoomListAdmin(admin.ModelAdmin):
    pass

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomMessage, RoomMessageAdmin)
admin.site.register(RoomList, RoomListAdmin)