from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^process_add$', views.process_add),
  # url(r'^process_del$', views.process_del),
  url(r'^$', views.index),
  url(r'course/destroy/(?P<id>\d+)$', views.delete)
]