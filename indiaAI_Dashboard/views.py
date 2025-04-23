from django.shortcuts import HttpResponse, render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def welcome(request):
    return render(request,'home.html')
    #return render(request,'index.html')

def show_login_form(request):
    return render(request,'login.html')


def submit_login_form(request):  # POST method
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('after_login')  # or your desired page
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')
    return redirect('show_login_form')  # fallback in case someone hits POST directly



def after_login(request):
    return render(request,'index.html')