from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    rn = serializers.IntegerField()
    class Meta:
        model = Student
        fields = '__all__'

    # def validate_rn(self, value):
    #     if Student.objects.get(rn=value):
    #         raise serializers.ValidationError('roll existed!')
    #     return value





