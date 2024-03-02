from django.db import models
import uuid
from django.core.validators import MinLengthValidator , RegexValidator
from rest_framework import serializers

# Create your models here.
class School(models.Model):
    School_name = {
        "J" : "Junior St Michal High School",
        "S" : "St karence Montensary Public School",
        "D" : "Doon Public School"
    }
    
    location_name = models.CharField(max_length=120)
    school_name = models.CharField(max_length=1 , choices=School_name)
    
class Student(models.Model):
    student_name = models.CharField(max_length=120 , default='Name')
    address = models.CharField(max_length=120)
    school_name = models.ForeignKey(School , on_delete=models.CASCADE)
    phone = models.CharField(max_length=15 , validators=[MinLengthValidator(10,message="mobile number must be at least 10 digit long"),RegexValidator(r'^9\d{9,14}',message='The nuber must be started with 9 and contain aat least 10 digit long')])
    age = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.student_name
    
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_name']  # Only include the field you want to display

class StudentSeralizer(serializers.ModelSerializer):
    school_name_display = serializers.SerializerMethodField()

    def get_school_name_display(self, obj):
        return obj.school_name.school_name  # Assuming the School model has a field named school_name

    class Meta:
        model = Student
        fields = ['student_name', 'address', 'school_name', 'school_name_display', 'phone', 'age']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        school_serializer = SchoolSerializer(instance.school_name)
        data['school_name'] = school_serializer.data  # Replace school ID with school name
        return data


        
    
        
        
    
    

    
    
    
