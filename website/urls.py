from django.contrib import admin
from django.urls import path
from article import views as article_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('', article_views.home, name ='home'),
    path('upload', article_views.upload, name='upload'),
    path('admin/', admin.site.urls),
    path('external', article_views.external)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)