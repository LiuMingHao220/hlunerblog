"""hluner_blog URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
import xadmin,os


urlpatterns = [
    path('',views.home,name='home'),
    path('blog/', include('blog.urls')),
    path('xadmin/', xadmin.site.urls),
    path('',include('django.contrib.auth.urls')),
    path('comment/', include('comment.urls')),
    path('likes/',include('likes.urls')),
    path('user/',include('user.urls')),
    path('markdown/', include('markdown_editor.urls')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('my_notifications',views.my_notifications,name='my_notifications'),
    path('<int:my_notification_pk>',views.my_notification,name='my_notification'),
    path('delete_my_read_notifications', views.delete_my_read_notifications, name='delete_my_read_notifications'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  # 添加图片的url


if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)

