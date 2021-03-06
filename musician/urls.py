from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musician.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'user.views.home_page', name='home'),
    url(r'^profile/', 'user.views.profile', name='profile'),
    url(r'^map/', 'user.views.map', name='map'),
    url(r'^new_user/', 'user.views.new_user', name='new_user'),
    url(r'^messages/', 'user.views.messages', name='messages'),
    url(r'^about/', 'user.views.about', name='about'),
    url(r'^donate/', 'user.views.donate', name='donate'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^splash/', 'user.views.splash', name='splash'),
    # ex. /search/oregon/portland/
    url(r'^search/(?P<user_state>.*)/(?P<user_city>.*)/$', 'user.views.search_city_state', name='search'),
    #url(r'^results/', 'user.views.results', name='search'),
    url(r'^all_users/', 'user.views.all_users', name='all_users'),
)
