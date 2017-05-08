from django.conf.urls import url
from django.views import static

from .. import views

urlpatterns = [
    url(r'^$', views.get_locations, name='get_locations'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'project/static'}),
]