from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method =="POST":
        
    form = LoginForm()
    return render(request,'users/login.html',{'form':form})