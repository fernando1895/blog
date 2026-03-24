from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='consolidacion_dashboard'),
    url(r'^asistencias/$', views.asistencia_list, name='consolidacion_list'),
    url(r'^asistencias/nueva/$', views.asistencia_new, name='consolidacion_new'),
    url(r'^asistencias/(?P<pk>\d+)/editar/$', views.asistencia_edit, name='consolidacion_edit'),
    url(r'^asistencias/(?P<pk>\d+)/eliminar/$', views.asistencia_delete, name='consolidacion_delete'),
]
