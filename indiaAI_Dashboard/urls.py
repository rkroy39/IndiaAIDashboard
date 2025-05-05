"""
URL configuration for indiaAI_Dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from indiaAI_Dashboard import views
from django.conf import settings
from django.conf.urls.static import static
from indiaAI_Dashboard.views.login import Login
from indiaAI_Dashboard.views.logout import Logout  
from indiaAI_Dashboard.views.home import Welcome
from indiaAI_Dashboard.views.after_login import AfterLogin
#from indiaAI_Dashboard.views import create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Welcome.as_view()),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('after-login/',AfterLogin.as_view(),name='after_login'),
    #path('create-user/', create_user, name='create_user'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])