"""AttractorGram2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from posts.views import feed
from rest_framework import routers
from api_v2.views import PostApiView, PostViewSet

router = routers.SimpleRouter()
router.register('postapi', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feed, name='feed'),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('', include(router.urls)),
    path('api_v2', PostApiView.as_view()),
    path('api_v2/<int:pk>', PostApiView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
