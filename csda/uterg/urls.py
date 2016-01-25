from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'uterg.views.home', name='uterg-home'),
    url(r'^graficos/$', 'uterg.views.graficos', name='uterg-graficos'),
    url(r'^equipamentos/$', 'uterg.views.equipamentos', name='equipamentos'),
    url(r'^graficos/$', 'uterg.views.graficos', name='graficos'),
    url(r'^relatorios/$', 'uterg.views.relatorios', name='relatorios-tecnicos'),
    url(r'^dados/$', 'uterg.views.dados', name='series-de-dados'),
]