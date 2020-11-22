from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User 
from .serializers import UserDetailsSerializer, UserSerializer
from .models import UserDetails 
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class CreateUserViewSet(viewsets.ModelViewSet):
    queryset= UserDetails.objects.all()
    serializer_class = UserDetailsSerializer


    def create(self, request):
        username = request.data['username']
        nickname = request.data['full_name']
        email = request.data['email']
        password = request.data['password']
        password2 = request.data['password2']
        phone = request.data['phone_number'] 

        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            data['response'] = 'User Created Successfully'
            data['username'] = user.username
            data['email'] = user.email

            my_user = User.objects.get(username=user)
            user_det = UserDetails.objects.create(user=my_user, nickname=nickname, phone_number=phone)
            user_det.save()

            
        else:
            data = serializer.errors
        return Response(data)


    def retrieve(self, request):
        print("Heyyyy")
        user = User.objects.all()

        data = {"data":user}
        return Response(data)

def jwt_response_payload_handler(token, user=None, request=None):
    username = request.data['username']
    
    try:
        user = User.objects.get(username=username)
        user_details = UserDetails.objects.get(user=user)
        print(user_details)
    except :
        return {"message":"Invalid details"}

    return {'token':token, 'full_name':user_details.nickname, 'phone':user_details.phone_number, 'id':user.id}

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate( attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        my_user = UserDetails.objects.get(user = self.user)

        data['id'] = my_user.id
        data['full_name'] = my_user.nickname
        data['phone'] = my_user.phone_number

        return data

    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




