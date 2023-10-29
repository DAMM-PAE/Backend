from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.InitDataBase.as_view()),
    path('bars/', views.BarList.as_view()),
    path('bars/<int:pk>/', views.BarDetail.as_view()),
    path('entregas/', views.EntregasList.as_view()),
    path('entregas/<int:pk>/', views.EntregasDetail.as_view()),
    path('facturamensual/', views.FacturaMensualList.as_view()),
    path('facturamensual/<int:pk>/', views.FacturaMensualDetail.as_view()),
    path('iot/', views.IOTList.as_view()),
    path('iot/<int:pk>/', views.IOTDetail.as_view()),
    path('prediccion/', views.PrediccionList.as_view()),
    #path('prediccion/<int:pk>/', views.PrediccionDetail.as_view()),
]
