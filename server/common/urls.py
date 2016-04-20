from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tags/list$', views.tags_list, name='common_tags_list'),
]