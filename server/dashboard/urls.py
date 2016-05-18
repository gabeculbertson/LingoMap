from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='dashboard_index'),
    url(r'^assigned_badge/(?P<pk>[0-9]+)/complete$', views.badge_mark_complete, name='dashboard_badge_complete'),
    url(r'^assigned_badge/(?P<pk>[0-9]+)/uncomplete$', views.badge_mark_uncomplete, name='dashboard_badge_uncomplete'),
]