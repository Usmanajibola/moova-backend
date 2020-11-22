from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from .models import *
import rest_framework_simplejwt.exceptions as exc
from api.models import UserDetails

class GetOrder(APIView):
    def post(self, request):
        try:
            print(request.data)
            customer_name = request.data['customer_name']
            phone = request.data['phone']
            pickup = request.data['pickup']
            destination = request.data['destination']
            price = request.data['price']

            available_rider = Rider.objects.filter(online=True)[0]

            data = {'rider_id':available_rider.id, 'rider':available_rider.user.username, 'phone':available_rider.phone_number, 'price':price, 'plate_number':available_rider.plate_number}
            #available_rider.online=False
            #available_rider.save()
            user = UserDetails.objects.get(nickname=customer_name).user
            user_details = UserDetails.objects.get(user=user)
            ride = Ride(user=user, price=price, pickup_location=pickup, destination=destination, rider=available_rider).save()
            RideHistory(ride=ride).save()

            return Response(data)
        except exc.InvalidToken:
            return Response({'message':'Authentication denied', status:401})



class CancelRide(APIView):
    def post(self, request):
        try:
            customer_name = request.data['customer_name']
            print(type(customer_name))

            my_user = UserDetails.objects.get(nickname=str(customer_name)).user
            print(my_user)
        
            ride = Ride.objects.get(user=my_user)
            ride.delete()

            return Response({'message':'Ride Cancelled'})

        except exc.InvalidToken:
           return Response({'message':'Authentication denied', status:401}) 
