from django.conf.urls import url
from django.views import static

from .. import views

urlpatterns = [
    url(r'^$', views.get_locations_client, name='get_locations'),
    url(r'^reserve_location/', views.reserve_location, name='reserve_location'),
    url(r'^my_bookings/', views.get_client_bookings, name='get_client_bookings'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'project/static'}),
]