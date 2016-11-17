from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_reg$', views.login_reg, name='login_reg'),
    url(r'^wall$', views.wall, name='wall'),
    url(r'^doodle$', views.doodle, name='doodle'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^logout$', views.logout, name='logout')
]
