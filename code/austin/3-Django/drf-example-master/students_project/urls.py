from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('apis/v1/', include('apis.urls')),
    path('user/', include('django.contrib.auth.urls')),    
    path('user/', include('users.urls')),
]
