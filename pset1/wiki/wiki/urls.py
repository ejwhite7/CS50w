"""wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import handler404, handler500, url
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('wiki/', include("encyclopedia.urls")),
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file")
]

handler404 = 'encyclopedia.views.handler404'
handler500 = 'encyclopedia.views.handler500'