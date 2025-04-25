from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerialzer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
    permission_classes = [IsAuthenticated]



class SuperAdminLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username,password=password)


        if user and user.is_superuser:
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh),"access":str(refresh.access_token)})
        return Response({"Error": "Invalid credenials or not superuser"},status=400)

class SuperUerLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response({"Message": "Successfully logged out"})
    