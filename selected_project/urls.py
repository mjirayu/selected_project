# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from restaurant import views as restaurant_views

urlpatterns = [
    url(r'^$', restaurant_views.HomeView.as_view(), name='home'),
    url(r'^search/$', restaurant_views.SearchView.as_view(), name='search'),
    url(r'^search/(?P<category>.*)/$', restaurant_views.SearchCategoryView.as_view(), name='category'),
    url(r'^admin/', include(admin.site.urls)),
]
