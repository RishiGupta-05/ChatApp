from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room, Message  # Importing Message model from your app's models module

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:25]  # Corrected slicing syntax

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
