from django.urls import path
from .views import student_list, students_detail

urlpatterns = [

    path('api/students/', student_list, name='list'),
    path('api/students/<int:pk>', students_detail, name='detail'),


]