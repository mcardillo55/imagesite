"""imagesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', 'images.views.signup'),
    url(r'^login/','images.views.login_view'),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    url(r'^profile/', 'images.views.profile'),
    url(r'^submit/', 'images.views.submit'),
    url(r'^delete/(?P<img_hash>.*)', 'images.views.delete', name='blah'),
    url(r'^latest/', 'images.views.latest'),
    url(r'^$', 'images.views.home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + [ url(r'(?P<img_hash>.*)', 'images.views.view'), ]
