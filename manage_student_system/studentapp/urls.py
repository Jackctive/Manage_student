from django.urls import path
from .views import danh_sach_sinh_vien, add_student, delete_student

urlpatterns = [
    path('', danh_sach_sinh_vien, name='ds_sv'),
    path('add-student/', add_student, name='add_student'),
    path('delete-student/<int:student_id>/', delete_student, name='delete_student'), 
]