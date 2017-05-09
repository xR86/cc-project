from django.conf.urls import url
from django.views import static

from .. import views

urlpatterns = [
    url(r'^$', views.book, name='book'),
    url(r'^add/', views.add_book, name='add_book'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'project/static'}),
]