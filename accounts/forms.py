# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

# مدل User پیش‌فرض جنگو را می‌گیریم
User = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    """
    فرم سفارشی برای ورود کاربر با استایل‌های Tailwind CSS.
    """
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-lg border p-3 text-sm focus:ring-amber-500 focus:border-amber-500', # استایل‌های Tailwind
            'placeholder': 'نام کاربری خود را وارد کنید'
        })
    )
    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full rounded-lg border p-3 text-sm focus:ring-amber-500 focus:border-amber-500', # استایل‌های Tailwind
            'placeholder': 'رمز عبور خود را وارد کنید'
        })
    )

    # یادداشت: فیلد 'remember me' به صورت پیش‌فرض در AuthenticationForm وجود ندارد.
    # اگر نیاز دارید، باید آن را به صورت دستی اضافه کنید.

class CustomUserCreationForm(UserCreationForm):
    """
    فرم سفارشی برای ثبت نام کاربر با اضافه کردن فیلدهای نام، نام خانوادگی، ایمیل
    و تأیید رمز عبور، همراه با استایل‌های Tailwind CSS.
    """
    # اضافه کردن فیلدهای مورد نیاز
    first_name = forms.CharField(
        label="نام",
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-lg border p-3 text-sm focus:ring-amber-500 focus:border-amber-500',
            'placeholder': 'نام خود را وارد کنید'
        })
    )
    last_name = forms.CharField(
        label="نام خانوادگی",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-lg border p-3 text-sm focus:ring-amber-500 focus:border-amber-500',
            'placeholder': 'نام خانوادگی خود را وارد کنید'
        })
    )
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(attrs={
            'class': 'block w-full rounded-lg border p-3 text-sm focus:ring-amber-500 focus:border-amber-500',
            'placeholder': 'example@example.com'
        })
    )
    # فیلد تأیید رمز عبور
    password2 = forms.CharField(
        label="تأیید رمز عبور",
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full rounded-lg border p-3 text-sm focus:ring-amber-500 focus:border-amber-500',
            'placeholder': 'رمز عبور خود را مجدداً وارد کنید'
        })
    )

    class Meta(UserCreationForm.Meta): # ارث‌بری از Meta کلاس والد
        model = User
        # اضافه کردن فیلدهای جدید به فیلدهای پیش‌فرض UserCreationForm
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def clean_password2(self):
        """
        تأیید می‌کند که رمز عبور دوم با رمز عبور اول مطابقت دارد.
        """
        password2 = self.cleaned_data.get("password2")
        if password2 and password2 != self.cleaned_data.get("password"):
            raise forms.ValidationError("رمزهای عبور مطابقت ندارند.")
        return password2

    def clean_email(self):
        """
        تأیید می‌کند که ایمیل قبلاً استفاده نشده است.
        """
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("این ایمیل قبلاً توسط کاربر دیگری استفاده شده است.")
        return email
