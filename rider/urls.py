from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'rider'



urlpatterns = [
    path(r'send_order_details/', views.GetOrder.as_view()),
    path(r'cancel_ride/', views.CancelRide.as_view())
]
