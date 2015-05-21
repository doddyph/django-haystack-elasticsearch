from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'haystack_dj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app_dj.views.home', name='home'),
    url(r'^about', 'app_dj.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
)
