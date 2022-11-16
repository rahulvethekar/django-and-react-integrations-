from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status 
from rest_framework.views import APIView
# Create your views here.

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request):
        data = request.data
        print(data)
        try:
            rn = data.get('rn')
            print('-----',rn)

            if Student.objects.filter(rn=rn):
                return Response({'error':'roll no already exited'})
            try:
                student_data = self.serializer_class(data=data)
                if student_data.is_valid():
                    student_data.save()
                    return Response(data)
                else:
                    return Response({'error':'invalid input to fields'})
            except Exception as e:
                return Response({'error':repr(e)})

        except Exception as e:
            return Response({'error':repr(e)})


class UpdateStudent(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self,request,pk):
        print(pk)
        print(request.data.get('rn'))
        try:
            stu_obj = Student.objects.get(rn=pk)
            student_serializer = StudentSerializer(stu_obj,data=request.data,partial=True)
            if student_serializer.is_valid():
                student_serializer.save()
                return Response(status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(repr(e))


class StudentById(APIView):

    def get(self,request,rn):
        try:
            student_obj = Student.objects.get(rn=rn)
            student_data = StudentSerializer(student_obj)
            # print(student_data.data)
            return Response(student_data.data)
        
        except Student.DoesNotExist:
            return Response({'error':'student does not exist!'})
    def delete(self,request,rn):
        try:
            Student.objects.get(rn=rn).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist as e:
            return Response(repr(e))
            

        
        
        

            

        



        
        

