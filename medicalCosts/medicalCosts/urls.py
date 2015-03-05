from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from diseases import views


router = routers.DefaultRouter()
router.register(r'diseases', views.DiseaseViewSet)
router.register(r'procedures', views.ProcedureViewSet)
router.register(r'operations', views.OperationViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    #url(r'^$', 'medicalCosts.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^diseases/', include('diseases.urls', namespace='diseases')),
)
