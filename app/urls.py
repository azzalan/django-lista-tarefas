from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from app.views import *

urlpatterns = [
    url(r'^tarefas/$',
        TarefaView.as_view(),
        name='tarefa'),
    url(r'^$', 
        RedirectView.as_view(url='tarefas/', permanent=False), 
        name='index')
]
