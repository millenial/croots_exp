from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import favfood.views

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'croots_exp.views.home', name='home'),
    # url(r'^croots_exp/', include('croots_exp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'food/$', 'favfood.views.getAllInformation'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', 'userinfo.views.main'),
    url(r'^movies/', 'fav_movie.views.listmovies'),
)
