from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from djangomain import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    ]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]



