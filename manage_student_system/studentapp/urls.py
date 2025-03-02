from django.urls import path
from .views import danh_sach_sinh_vien

urlpatterns = [
    path('', danh_sach_sinh_vien, name='ds_sv'),
]