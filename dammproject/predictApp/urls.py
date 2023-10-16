from django.urls import path
from . import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='helloworld/', permanent=True)),
    path('helloworld/', views.helloworld, name='helloworld'),
    path('inicializarBaseDatos/', views.inicializarBaseDatos, name='inicializarBaseDatos'),
]