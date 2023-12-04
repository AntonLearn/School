from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'school/students_list.html'
    ordering = 'group'
    queryset = Student.objects.all().order_by(ordering).prefetch_related('teachers')