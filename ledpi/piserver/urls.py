from django.conf.urls import url

from . import views

app_name = 'piserver'
urlpatterns = [
    # /piserver/ 
    url(r'^$', views.index, name='index'),

    # /piserver/2/
    url(r'^(?P<light_id>[0-9]+)/$', views.detail, name='detail'),

    # /piserver/2/results/
    url(r'^(?P<light_id>[0-9]+)/results/$', views.results, name='results'),
    # /polls/2/flip/
    url(r'^(?P<light_id>[0-9]+)/flip/$', views.flip, name='flip'),
]
