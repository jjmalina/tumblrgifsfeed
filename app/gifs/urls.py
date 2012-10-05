from django.conf.urls import patterns, include, url

urlpatterns = patterns('gifs.views',
    url(r'', 'index'),
)
