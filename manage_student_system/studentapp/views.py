from django.shortcuts import render
from .models import SinhVien

def danh_sach_sinh_vien(request):
    sinhviens = SinhVien.objects.all()  # Lấy tất cả sinh viên từ database
    context = {'sinhviens': sinhviens}

    return render(request, 'students/index.html', context)

def add_student(request):
    return render(request, 'students/add_student.html')
