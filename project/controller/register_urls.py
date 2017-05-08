from django.conf.urls import url
from django.views import static

from .. import views

urlpatterns = [
    url(r'^$', views.register, name='index'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'project/static'}),
]