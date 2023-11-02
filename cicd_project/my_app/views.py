from django.shortcuts import render
from .models import MyUser

def home(request):
    users = MyUser.objects.all()
    return render(request, 'my_app/index.html',{'users' : users})