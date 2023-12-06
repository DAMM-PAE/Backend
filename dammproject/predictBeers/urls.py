from django.urls import path
from . import views
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Predict Beers API')

urlpatterns = [
    # path('', schema_view),
    path('bars/', views.BarList.as_view()),
    path('bars/<int:pk>/', views.BarDetail.as_view()),
    path('bars/<int:id>/update', views.dataUpdate),
    path('entregas/', views.EntregasList.as_view()),
    path('entregas/<int:pk>/', views.EntregasDetail.as_view()),
    path('facturamensual/', views.FacturaMensualList.as_view()),
    path('facturamensual/<int:pk>/', views.FacturaMensualDetail.as_view()),
    # path('iot/', views.IOTList.as_view()),
    # path('iot/<int:pk>/', views.IOTDetail.as_view()),
    path('init/', views.InitData.as_view()),
]
