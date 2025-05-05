from django.views import View
from django.shortcuts import HttpResponse, render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from indiaAI_Dashboard.models import LoginAuditTrail
class Login(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            #print(username)
            password = request.POST.get('password')
            #print(password)
            user = authenticate(request, username=username, password=password)
            #print(user)
        if user:
            login(request, user)
            ip_address = get_client_ip(request)
            LoginAuditTrail.objects.create(
            user=user if user else None,
            username_attempted=username,
            success=True if user else False,
            ip_address=ip_address
        )
            request.session['username'] = username

            return redirect('after_login')  # Redirect to a success page or dashboard
            #return render(request,'index.html')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')
    
    
def get_client_ip(request):
    """Safely extract client IP address even behind proxies."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # first IP in list
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip