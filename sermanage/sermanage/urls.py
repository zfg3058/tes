"""sermanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from counter.views import *
from servers.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #counter app
    url(r'^$',                          index,              name='index'),
    url(r'^login/$',                    login,              name='login'),
    url(r'^logins/$',                   logins),
    url(r'^tab/$',                      tab,                name='tab'),
    url(r'^add/$',                      add,                name='add'),
    url(r'^adv/$',                      adv,                name='adv'),
    url(r'^book/$',                     book,               name='book'),
    url(r'^cate/$',                     cate,               name='cate'),
    url(r'^cateedit/$',                 cateedit,           name='cateedit'),
    url(r'^column/$',                   column,             name='column'),
    url(r'^info/$',                     info,               name='info'),
    url(r'^list/$',                     list,               name='list'),
    url(r'^page/$',                     page,               name='page'),
    url(r'^passwd/$',                   passwd,             name='passwd'),
    url(r'^tips/$',                     tips,               name='tips'),
    url(r'^usergroup/$',                usergroup,          name='usergroup'),
    url(r'^users/$',                    users,              name='users'),
    url(r'^adduser/$',                  adduser,            name='adduser'),
#     url(r'^main/$', main),
    #servers app
#     url(r'^sertest/$', sertest),
]
