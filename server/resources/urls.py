from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='resources_index'),
    url(r'^(?P<rid>[0-9]+)/$', views.detail, name='resources_detail'),
    url(r'^add$', views.add_media, name='resources_add'),
    url(r'^edit/(?P<rid>[0-9]+)$', views.edit_media, name='resources_edit'),
]