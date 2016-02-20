from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
# we are assigning a view called post_list to ^$ url
# so this regular expression will match a beginning ^ followed
# by an end - so only empty strings will match
