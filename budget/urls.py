from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='budget_dashboard'),
    url(r'^transacciones/$', views.transaction_list, name='transaction_list'),
    url(r'^transacciones/nueva/$', views.transaction_new, name='transaction_new'),
    url(r'^transacciones/(?P<pk>\d+)/editar/$', views.transaction_edit, name='transaction_edit'),
    url(r'^transacciones/(?P<pk>\d+)/eliminar/$', views.transaction_delete, name='transaction_delete'),
    url(r'^categorias/$', views.category_list, name='category_list'),
    url(r'^categorias/nueva/$', views.category_new, name='category_new'),
    url(r'^categorias/(?P<pk>\d+)/editar/$', views.category_edit, name='category_edit'),
    url(r'^categorias/(?P<pk>\d+)/eliminar/$', views.category_delete, name='category_delete'),
]
