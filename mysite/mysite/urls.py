"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from accounts.views import (
    home_view, gallery_view, board_list_view, 
    board_detail_view, board_write_view, 
    gallery_detail_view, gallery_write_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('board/', include('board.urls')),
    path('', home_view, name='home'),
    # HTML 페이지들을 위한 임시 URL
    path('gallery.html', gallery_view, name='gallery'),
    path('board_list.html', board_list_view, name='board_list'),
    path('board_detail.html', board_detail_view, name='board_detail'),
    path('board_write.html', board_write_view, name='board_write'),
    path('gallery_detail.html', gallery_detail_view, name='gallery_detail'),
    path('gallery_write.html', gallery_write_view, name='gallery_write'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)