from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cars/', include('cars.urls')),
    path('admin/', admin.site.urls),
]

static_media_urls = (
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    +
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

urlpatterns += static_media_urls