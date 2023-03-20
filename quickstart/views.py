from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# READ operation
@api_view(['GET'])
def home(request):
    student_obj=Student.objects.all()
    serializer=StudentSerializer(student_obj,many=True)
    return Response(serializer.data)
# CREATE operation
@api_view(['POST'])
def post_student(request):
    student_obj=Student.objects.all()
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# UPDATE operation
@api_view(['POST'])
def update_student(request,id):
    student_obj=Student.objects.get(id=id)
    serializer=StudentSerializer(instance=student_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# DELETE operation
@api_view(['DELETE'])
def delete_student(request,id):
    student_obj=Student.objects.get(id=id)
    student_obj.delete()
    return Response("Student is deleted! ")
