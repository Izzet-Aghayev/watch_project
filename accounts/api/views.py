from urllib import request
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .serializers import (
    LoginSerializer,
    RegisterSerializer,

)


# Function base views (api)

@api_view(['POST'])
def sign_in(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        username = serializer.validated_data.get('username')        # Serializerə göndərilən username-ni alır
        password = serializer.validated_data.get('password')        # Serializerə göndərilən password-u alır
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)        # İstifadəçini login edir
            return Response({'detail': 'Lohin oldunuz'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Yanlış istifadəçi adı və ya parol.'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
{
"username":"admin",
"password":"Izzet-1409"
}
'''


@api_view(['POST'])
def sign_out(request):
    logout(request)         # İstifadəçi sesiyasını bitirir

    return Response({'detail':'Logout oldunuz'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        User.objects.create_user(username=username, password=password)      # Yeni user obyekti yaradır
        return Response({'detail': 'Register oldunuz'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
{
"username":"excample1",
"password":"Izzet-1409"
}
'''


# Class base views (api)

class LoginView(APIView):
    def post(self, request):
        if request.method=='POST':
            serializer = LoginSerializer(data=request.data)

            if serializer.is_valid():
                username = serializer.validated_data.get('username')    # Serializerə göndərilən username-ni alır
                password = serializer.validated_data.get('password')    # Serializerə göndərilən password-u alır

                user = authenticate(request, username=username, password=password)      # Yoxlanış edir

                if user is not None:
                    login(request, user)        # Sesiyanı başladır
                    return Response({'detail':'Login oldunuz'}, status=status.HTTP_200_OK)
                
                return Response({'detail': 'Yanlış istifadəçi adı və ya parol.'}, status=status.HTTP_401_UNAUTHORIZED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
'''
{
"username":"admin",
"password":"Izzet-1409"
}
'''

class LogoutView(APIView):
    def post(self, request):
        logout(request)     # Sesiyanı bitirir
        return Response({'detail':'Logout oldunuz'}, status=status.HTTP_200_OK)


class RegisterView(APIView):
    def post(self, request):
        if request.method=='POST':
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.validated_data.get('username')
                password = serializer.validated_data.get('password')

                User.objects.create_user(username=username, password=password)      # Yeni user obyekti yaradır
                return Response({'detail': 'Register oldunuz'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
{
"username":"excample1",
"password":"Izzet-1409"
}
'''