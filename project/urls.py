from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_analytics.urls', namespace="social_analytics")),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#For Worker
urlpatterns += patterns('',
    (r'^django-rq/', include('django_rq.urls')),
)
