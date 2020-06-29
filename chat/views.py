from django.shortcuts import render,redirect
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    if request.method=="POST":
        data = request.POST.get("just")
        if User.objects.filter(username = data).exists():
            user=User.objects.get(username=data)

            login(request,user)
        else:
            user=User.objects.create_user(username=data,password=data)
            login(request,user)

        return redirect("room", room_name="test")

    else:
        return render(request,"chat/index.html")

def room(request, room_name):
    data = request.POST.get('god')
    print(data)
    messages=Message.objects.all()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messagesfromdb':messages
    })