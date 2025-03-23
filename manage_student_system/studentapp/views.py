from django.shortcuts import render
from .models import SinhVien
from django.shortcuts import redirect
from django.contrib import messages

def danh_sach_sinh_vien(request):
    sinhviens = SinhVien.objects.all()  # Lấy tất cả sinh viên từ database
    context = {'sinhviens': sinhviens}

    return render(request, 'students/index.html', context)

def add_student(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        mssv = request.POST.get('mssv')
        ho_ten = request.POST.get('ho_ten')
        ngay_sinh = request.POST.get('ngay_sinh')
        email = request.POST.get('email')
        so_dien_thoai = request.POST.get('so_dien_thoai')
        lop = request.POST.get('lop')
        nganh_hoc = request.POST.get('nganh_hoc')  

        new_student = SinhVien(mssv=mssv, ho_ten=ho_ten, ngay_sinh=ngay_sinh, email=email, so_dien_thoai=so_dien_thoai, lop=lop, nganh_hoc=nganh_hoc)

        # Ceate new student and save to database
        try:
            # Save the new student to the database
            new_student.save()
            
            messages.success(request, "Sinh viên đã được thêm thành công!")
            print("Sinh viên đã được thêm thành công!")

            return redirect('ds_sv')  # Redirect to the student list page

        except Exception as e:
            messages.error(request, f"Đã xảy ra lỗi: {e}")
            print(f"Đã xảy ra lỗi: {e}")
    return render(request, 'students/add_student.html')
