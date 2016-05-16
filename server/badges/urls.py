from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='badges_index'),
    url(r'^(?P<rid>[0-9]+)/$', views.detail, name='badges_detail'),
    url(r'^(?P<pk>[0-9]+)/addto/', views.addto, name='badges_addto'),
    url(r'^add$', views.BadgeCreateView.as_view(), name='badges_add'),
    url(r'^edit/(?P<pk>[0-9]+)', views.BadgeUpdateView.as_view(), name='badges_update'),
    url(r'^add_tag', views.BadgeTagAddView.as_view(), name='badges_add_tag'),
    url(r'^flag_tag', views.BadgeTagFlagView.as_view(), name='badges_flag_tag'),
]