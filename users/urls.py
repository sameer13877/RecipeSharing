from rest_framework.routers import DefaultRouter
from .views import UserViewset, SuperAdminLoginView,SuperUerLogoutView
from django.urls import path, include


router = DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', SuperAdminLoginView.as_view(),name = "superuser-login"),
    path('logout/',SuperUerLogoutView.as_view(),name = "superuser-logout"),

]