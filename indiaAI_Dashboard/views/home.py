
from django.shortcuts import HttpResponse, render,redirect
from django.views import View


class Welcome(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        return HttpResponse("This is a POST request")
