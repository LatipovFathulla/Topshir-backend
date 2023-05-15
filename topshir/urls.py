from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from topshir import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staticpages.urls'), name='pages')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)