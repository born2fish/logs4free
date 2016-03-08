from django.conf.urls import include, url
from django.contrib import admin
from apache_an.views import ApacheLogsPage, LastLogPage, ApacheErrorsPage

urlpatterns = [
    # Examples:
    # url(r'^$', 'log4free.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', ApacheLogsPage.as_view(), name='ApacheLogsPage'),
    url(r'^last/$', LastLogPage.as_view(), name='LastLogPage'),
    url(r'^errors/$', ApacheErrorsPage.as_view(), name='ApacheErrorsPage'),

    url(r'^admin/', include(admin.site.urls)),
]
