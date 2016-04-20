from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='badges_index'),
    url(r'^(?P<rid>[0-9]+)/$', views.detail, name='badges_detail'),
    url(r'^add$', views.BadgeCreateView.as_view(), name='badges_add'),
    url(r'^edit/(?P<pk>[0-9]+)', views.BadgeUpdateView.as_view(), name='badges_update'),
    url(r'^add_tag', views.BadgeTagAddView.as_view(), name='badges_add_tag'),
]