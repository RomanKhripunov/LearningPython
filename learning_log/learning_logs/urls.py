from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),                                          # Home page
    url(r'^topics/$', views.topics, name='topics'),                                 # All topics
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),                 # Requested topic
]
