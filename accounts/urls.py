# accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views # برای استفاده از viewهای آماده جنگو
from . import views # viewهای سفارشی خودمان

urlpatterns = [
    # صفحه ورود (Login)
    # از View سفارشی خودمان که فرم و تمپلیت لاگین را مدیریت می‌کند
    path('login/', views.CustomLoginView.as_view(), name='login'),

    # صفحه خروج (Logout)
    # از View آماده جنگو استفاده می‌کنیم
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # صفحه ثبت نام (Register)
    # از View سفارشی خودمان که فرم ثبت نام را مدیریت می‌کند
    path('register/', views.CustomRegisterView.as_view(), name='register'),

    # (اختیاری) صفحه فراموشی رمز عبور - اگر نیاز داشتی اضافه کن
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
