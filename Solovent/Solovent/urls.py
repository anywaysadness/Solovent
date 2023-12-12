from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

from web.views import IndexView

admin.site.site_header = "Solovent"
admin.site.index_title = "Admin panel"


# Список всех страниц сайта (При переходе на www.solovent.com/admin/ выдает страницу admin.site.urls)
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('store/', include('store.urls', namespace='store')),
    path('create/', include('web.urls', namespace='web')),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.STATIC_URL, documen_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)