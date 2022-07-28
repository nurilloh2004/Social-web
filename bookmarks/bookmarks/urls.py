
from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('account/', include('account.urls')),
    re_path('social-auth/', include('social_django.urls', namespace='social')),
    re_path('images/', include('images.urls', namespace='images')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)