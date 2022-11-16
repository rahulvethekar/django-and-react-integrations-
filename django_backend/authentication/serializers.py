from rest_framework import serializers
from django.contrib.auth.models import User



class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

    def create(self, validated_data):
        user = super(SignUpSerializer,self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']

    

