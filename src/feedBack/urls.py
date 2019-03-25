"""feedBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from dataStorage import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    #url(regex, view, kwargs=None, name=None),
    #url(regex, view, include('<appName>.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^feedBack/', include('dataStorage.urls')),
]

#requied on deploy
#from .settings.production import *#(STATIC_URL ,STATIC_ROOT ,MEDIA_URL ,MEDIA_ROOT)
#from .settings.local import *

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
