from django.conf.urls import url
from .views_api import Animal

urlpatterns = [
    url(r'^animal/$', Animal.as_view()),
    url(r'^animal/(?P<pk>[0-9]+)/$', Animal.as_view()),
]
