from django.conf.urls import url
from django.views import static

from .. import views

urlpatterns = [
    url(r'^$', views.get_register_page, name='index'),
    url(r'^verified/', views.register, name='register'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'project/static'}),
]