from django.conf.urls import url
from django.views import static

from .. import views

urlpatterns = [
    url(r'^$', views.get_locations_provider, name='get_locations_provider'),
    url(r'^get_reservations/', views.get_reservations_provider, name='get_reservations_provider'),
    url(r'^confirm_reservation', views.confirm_reservations_provider, name='confirm_reservations_provider'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'project/static'}),
]