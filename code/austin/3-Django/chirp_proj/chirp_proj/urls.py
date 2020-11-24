from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chirp_app.urls')),
] + static(settings.MEDIA_URL, doctument_root=settings.MEDIA_ROOT)