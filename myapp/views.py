from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import StudentSerializer
from .models import Student

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls= {
        'List': '/list/',
        'Detail View': '/detail/<int:id>/',
        'Create': '/create/',
        'Update': '/update/<int:id>/',
        'Delete': '/delete/<int:id>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def StudentAll(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def StudentList(request,pk):
    student = Student.objects.all()
    total = student.count()
    total_page = (total//6)+1
    y= pk*6
    x=y-5
    per_page = 6
    data = Student.objects.filter(id__range=(x,y))
    serializer = StudentSerializer(data, many=True)
    api_details = {
        'page': pk,
        'per_page': per_page,
        'total': total,
        'total_pages':total_page ,
        'data': serializer.data,
    }
    return Response(api_details)