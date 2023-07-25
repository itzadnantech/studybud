from django.shortcuts import render
from .models import Room
 
# Create your views here.

# rooms = [
#     {'id':1,"name":"lets learn Python"},
#     {'id':2,"name":"Design with me"},
#     {'id':3,"name":"Frontend Developer"},
# ]

# Load home page
def home(request):
    rooms = None
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'base/home.html',context)

# Load room page
def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {"room":room}
    return render(request,'base/room.html',context)