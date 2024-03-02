from django.shortcuts import render
from .models import Student , School , StudentSeralizer , SchoolSerializer
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response

# Create your views here.
class SchoolDetailView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeralizer
    
class StudentRetriveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeralizer

