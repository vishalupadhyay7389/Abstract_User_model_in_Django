from django.urls import path
from api.views import StudentListView , StudentRetriveView , SchoolDetailView

urlpatterns = [
    path('api/', StudentListView.as_view() , name="student"),
    path('api/<int:pk>/', StudentRetriveView.as_view() , name="student"),
    path('school/', SchoolDetailView.as_view() , name="school"),
    
]