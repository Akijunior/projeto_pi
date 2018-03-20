"""active_gears URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('wrnpro', ),
}

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/',  JavaScriptCatalog.as_view(packages=[js_info_dict]), name='javascript-catalog'),
    path('rosetta/', include('rosetta.urls')),

    path('admin/', admin.site.urls),
    path('', include('account.urls'), name='conta'),
    path('', include('core.urls'), name='core'),
]
