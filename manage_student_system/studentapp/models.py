from django.db import models

# Create your models here.
class SinhVien(models.Model):
    mssv = models.CharField(max_length=10, unique=True)  # Mã số sinh viên
    ho_ten = models.CharField(max_length=100)
    ngay_sinh = models.DateField()
    email = models.EmailField(unique=True)
    so_dien_thoai = models.CharField(max_length=10, blank=True, null=True)
    lop = models.CharField(max_length=50)
    nganh_hoc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.mssv} - {self.ho_ten}"
