from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from djangomain import settings

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root':
                                             settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':
                                              settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
