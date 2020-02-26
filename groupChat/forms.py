from django import forms
from groupChat.models import GroupUser, GroupMessage

class GroupUserForm(forms.ModelForm):
    class Meta:
        model = GroupUser
        fields = ['name']

class GroupMessageForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['content', 'owner']
        