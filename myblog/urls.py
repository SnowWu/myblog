"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.contrib import staticfiles
from django.conf.urls import url
from django.contrib import admin
from article import views


urlpatterns = [
    url(r'^admin/', admin.site.urls), #可以使用设置好的url进入网站后台
    url(r'^$', views.home, name = 'home'),
    #url(r'^(?P<my_args>\d+)/$', views.detail, name = 'detail'),
    #url(r'^test/$', views.test)
    url(r'^(?P<id>\d+)/$', views.detail, name = 'detail'),
]
#urlpatterns += staticfiles_urlpatterns()