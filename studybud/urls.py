
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include

  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
]
