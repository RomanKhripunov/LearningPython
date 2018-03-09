from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^(?P<post_id>\d+)/edit_post/$', views.edit_post, name='edit_post'),
]
