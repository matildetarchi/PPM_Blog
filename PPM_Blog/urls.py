from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("TheBlog.urls")),
    path("admin/", admin.site.urls),
    path("users/", include('django.contrib.auth.urls')),
    path("users/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)