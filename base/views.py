from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q

# Create your views here.

# rooms = [
#     {'id':1,"name":"lets learn Python"},
#     {'id':2,"name":"Design with me"},
#     {'id':3,"name":"Frontend Developer"},
# ]


# Load home page
def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = None
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)
        | Q(name__icontains=q)
        | Q(description__icontains=q)
        | Q(host__username__icontains=q)
    )
    rooms_count = rooms.count()
    topics = Topic.objects.all()
    context = {"rooms": rooms, "topics": topics, "rooms_count": rooms_count}
    return render(request, "base/home.html", context)


# Load room page
def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)


# Create new is here
def createRoom(request):
    form = RoomForm()

    # New Entry
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


# update a room
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


# update a room
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})
