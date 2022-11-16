from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import SignUpSerializer,UserDataSerializer
from django.contrib.auth.models import User

# Create your views here.


class SignUpApiView(APIView):

    def post(self,request):

        try:
            user_data = request.data
            user_serializer = SignUpSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response(repr(e))
    
    def get(self,request):
        try:
            users = User.objects.all()
            users_serializer = UserDataSerializer(users,many=True)
            print(users_serializer.data)
            return Response(users_serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(repr(e))

