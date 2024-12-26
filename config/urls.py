from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('Ims/', include('Ims.urls', namespace='Ims')),
    path('users/', include('users.urls', namespace='users'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)