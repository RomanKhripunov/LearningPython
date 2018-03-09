from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),                                          # Home page
    url(r'^topics/$', views.topics, name='topics'),                                 # All topics
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),                 # Requested topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),                        # Page of creating a new topic
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),      # Create new entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),   # Edit entry
]
