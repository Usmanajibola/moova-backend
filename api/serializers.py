from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

from .models import UserDetails


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'inpot_type':'password'}, write_only=True)
    class Meta:
        model=User
        fields= ['id','username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        print(email)

        if password != password2:
            raise serializers.ValidationError('password mismatch')

        if User.objects.filter(email__iexact=email):
            raise serializers.ValidationError('Email already exists')

        user = User.objects.create(
            email = email,
            username= username,
        )

        user.set_password(password)
        user.save()

        return user



class UserDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserDetails
        fields = ['id', 'user', 'nickname', 'phone_number']
