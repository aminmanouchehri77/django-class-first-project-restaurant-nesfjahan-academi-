from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # اگر آدرس‌های اپ restaurant را در فایل جداگانه نوشته‌ای:
    path('', include('restaurant.urls')),
    path('accounts/', include('accounts.urls')),
]

# فقط هنگام توسعه با DEBUG=True
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
