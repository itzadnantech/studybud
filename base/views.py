from django.shortcuts import render , redirect
from .models import Room
from .forms import RoomForm
 
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

# Create new is here
def createRoom(request):
    form = RoomForm()

    # New Entry
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form} 
    return render(request,'base/room_form.html',context)



# update a room
def updateRoom(request,pk):
    print("update Room")


# update a room   
def deleteRoom(request,pk):
    print("Delete Room")