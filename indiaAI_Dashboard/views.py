from django.shortcuts import HttpResponse, render


def welcome(request):
    return render(request,'home.html')
    #return render(request,'index.html')

def loginPage(request):
    return render(request,'login.html')