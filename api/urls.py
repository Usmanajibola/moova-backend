from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter()

router.register(r'signup', CreateUserViewSet)




app_name='api'


urlpatterns=[
   path(r'', include(router.urls)),
   path('api-token-auth/', MyTokenObtainPairView.as_view(), name="obtain_token"),
   path('api-token-refresh/', TokenRefreshView.as_view(), name="refresh_token")
]