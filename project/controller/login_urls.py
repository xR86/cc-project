from django.conf.urls import url
from django.views import static

from .. import views

urlpatterns = [
    url(r'^$', views.get_login_page, name='index'),
    url(r'^verified/', views.login, name='login'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'project/static'}),
]