from django.conf.urls import patterns, url
from diseases import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^disease/(?P<disease_id>\d+)/$', views.disease, name='disease'),
  url(r'^add_disease/$', views.add_disease, name='add_disease'),
  url(r'^procedure/(?P<procedure_id>\d+)/$', views.procedure, name='procedure'),
  url(r'^operation/(?P<operation_id>\d+)/$', views.operation, name='operation'),
)
