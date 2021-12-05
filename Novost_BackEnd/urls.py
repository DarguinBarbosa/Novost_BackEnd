from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.urls.conf import re_path
from apps.users.views import Login, LogOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.users.api.urls')),
    path('', Login.as_view(), name = 'Login'),
    path('Logout', LogOut.as_view(), name = 'Logout'),
    path('novedades/', include('apps.novedades.api.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_ROOT)
