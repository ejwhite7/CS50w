from django.urls import path, re_path
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name="index"),
    path('new', views.new, name='new'),
    path('random/', views.randomPage, name='random'),
    path('search', views.search, name='search'),
    path('<str:entry>/', views.entry, name='entry'),
    path('edit', views.edit, name='edit'),
    
]

handler404 = views.handler404
handler500 = views.handler500