"""
URL configuration for dj_folder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from app_travel.views import coming_soon


if settings.COMING_SOON_MODE:
    urlpatterns = [
        re_path(r'^.*$', coming_soon),
    ]
else:
    urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('app_travel.urls')),
    path('blog/', include('app_blog_travel.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^.*$', coming_soon),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)