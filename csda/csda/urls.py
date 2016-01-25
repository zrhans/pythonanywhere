"""csda URL Configuration

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
from django.conf.urls import patterns,include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$','csda.views.home'),
    url(r'^admin/', admin.site.urls),



    url(r'^uterg/', include('uterg.urls'), name='uterg'),

    # user auth urls
    #5 novas urls exigem 5 novos metodos na view.py

    url(r'^accounts/login/$', 'csda.views.login', name='login'),
    url(r'^accounts/auth/$', 'csda.views.auth_view', name='auth'),
    url(r'^accounts/logout/$', 'csda.views.logout', name='logout'),
    url(r'^accounts/loggedin/$', 'csda.views.loggedin', name='loggedin'),
    url(r'^accounts/invalid/$', 'csda.views.invalid_login', name='invalid'),


]
