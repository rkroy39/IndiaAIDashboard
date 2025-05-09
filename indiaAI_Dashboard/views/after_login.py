from django.views import View
from django.shortcuts import render,redirect
from django.contrib import messages

class AfterLogin(View):
    def get(self, request):
        if request.session.has_key('username'):
           username = request.session['username']
           print(username)
           #messages.success(request, "You have been logged out.")
           return render(request,'index.html')
        else:
            #messages.success(request, "You are not logged in...Please login to continue")
            return redirect('login')