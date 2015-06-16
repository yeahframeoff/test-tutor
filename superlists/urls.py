from django.conf.urls import include, url
from django.contrib import admin

from lists import views as listviews

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', listviews.home_page, name='home'),
    url(r'^lists/new$', listviews.new_list, name='new_list'),
    url(r'^lists/(\d+)/$', listviews.view_list, name='view_list'),
    url(r'^lists/(\d+)/add_item$', listviews.add_item, name='add_item'),
]
