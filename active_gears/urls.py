from django.contrib import admin

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/',  JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('rosetta/', include('rosetta.urls')),

    path('admin/', admin.site.urls),
    path('', include('account.urls'), name='conta'),
    path('', include('core.urls'), name='core'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


