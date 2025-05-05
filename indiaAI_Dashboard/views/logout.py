from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout

class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('/')