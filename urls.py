# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.auth.views import *
from django.contrib import admin
from ltichf.lt.views import *

admin.autodiscover()

urlpatterns = patterns('',
#	(r'^data/$', data_atual),
#	(r'^data/plus/\d{1,2}/$', horas_depois),
    (r'^admin/', include(admin.site.urls)),
	
    (r'^adicionar/(?P<tpObjeto>\w+)/(?P<idObjeto>\d+)/$', adicionar),
    (r'^exibir/(?P<tpObjeto>\w+)/(?P<idObjeto>\d+)/$', exibir),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    )
