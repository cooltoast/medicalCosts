from django.conf.urls import patterns, url
from diseases import views

urlpatterns = patterns('',
  url(r'^$', views.operations, name='operations'),
)
