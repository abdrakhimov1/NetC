# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http  import require_GET, require_POST
from groupChat.forms import GroupUserForm, GroupMessageForm
from django.apps import apps


@csrf_exempt
@require_POST
def dreateUser(request):
    