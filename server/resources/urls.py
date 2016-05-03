from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='resources_index'),
    url(r'^(?P<rid>[0-9]+)/$', views.detail, name='resources_detail'),
    url(r'^(?P<rid>[0-9]+)/fav$', views.favorite, name='resources_fav'),
    url(r'^(?P<rid>[0-9]+)/unfav$', views.unfavorite, name='resources_unfav'),
    url(r'^add$', views.StudyMediaCreateView.as_view(), name='resources_add'),
    url(r'^add_tag', views.MediaTagAddView.as_view(), name='resources_add_tag'),
    url(r'^flag_tag', views.MediaTagFlagView.as_view(), name='resources_flag_tag'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.StudyMediaUpdateView.as_view(), name='resources_edit'),
]