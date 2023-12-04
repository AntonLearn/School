from django.urls import path

# from school.views import students_list
from school.views import StudentListView

urlpatterns = [
    path('', StudentListView.as_view(), name='students'),
]
