from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('superuser/', include('users.urls')),
    path('', include('recipes.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name = 'token_refresh'),

]
