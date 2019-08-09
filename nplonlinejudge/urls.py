"""nplonlinejudge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from . import views

admin.site.site_header = 'Nepal Online Judge Admin'
admin.site.site_title = 'Admin Panel'
admin.site.index_title = 'NPLOJ'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('index/', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('programmers/', include('programmers.urls')),
    path('problemsets/', include('problemsets.urls')),
    path('profile/', include('programmers.urls')),
    path('submissions/', include('submissions.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
