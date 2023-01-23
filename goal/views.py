from django.shortcuts import render, redirect
from .models import Blog, Room, Messages,User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages




# Create your views here.
def index(request):

    blogs = Blog.objects.all()

    return render(request, "index.html", {"blogs": blogs})

def blog(request, pk):

    blogs = Blog.objects.get(id = pk)

    return render(request, "blog.html", {"blogs":blogs, "pk":pk })


def room(request):
    available_rooms = Room.objects.all()
    all_msg = len(Messages.objects.all())

    all_room = len(Room.objects.all())

    return render(request, 'room.html', {'available_rooms':available_rooms, 'all_msg':all_msg, 'all_room':all_room})

def new_room(request):
    return render(request, 'new_room.html')

def chat_room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name = room)
    return render(request, 'chat_room.html', {'username':username, 'room':room,'room_details':room_details})

def checkroom(request):
    username = request.POST['username']
    room = request.POST['room']

    if Room.objects.filter(name=room).exists():
        return redirect('new-room/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('new-room/'+room+'/?username='+username)

def send(request):
    username = request.POST['username']
    room_id = request.POST['room_id']
    messages = request.POST['message']

    recent_chat = Messages.objects.create(username=username, room=room_id, messages=messages)
    recent_chat.save()
    return HttpResponse("Message sent")

def receivemessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Messages.objects.filter(room=room_details.id)
    

    return JsonResponse({'messages':list(messages.values())})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email already exists on our database')
                return redirect('register')
            else:
                fresh_user = User.objects.create_user(username=username, email=email,password=password)
                fresh_user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



