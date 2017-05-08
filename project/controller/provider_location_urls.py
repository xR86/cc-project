from django.conf.urls import url
from django.views import static

from .. import views

urlpatterns = [
    url(r'^$', views.get_locations_provider, name='get_locations_provider'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'project/static'}),
]