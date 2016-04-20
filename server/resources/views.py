from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

from .models import StudyMedia, StudyMediaTags

from common.views import TagAddView

from dashboard.models import UserResources

class StudyMediaForm(ModelForm):
    class Meta:
        model = StudyMedia
        fields = ['title', 'description', 'type', 'image', 'guide_text']


class StudyMediaCreateView(CreateView):
    form_class = StudyMediaForm
    template_name = 'resources/edit.html'


class StudyMediaUpdateView(UpdateView):
    form_class = StudyMediaForm
    model = StudyMedia
    template_name = 'resources/edit.html'


def index(request):
    media = StudyMedia.objects.all()

    return render(request, 'resources/index.html', context={'media': media})


def detail(request, rid):
    media = get_object_or_404(StudyMedia, pk=rid)

    added = False

    if request.user.is_authenticated():
        try:
            UserResources.objects.get(user=request.user, resource=media)
            added = True
        except UserResources.DoesNotExist:
            pass

    return render(request, 'resources/detail.html', context={'m': media, 'added': added})


class MediaTagAddView(TagAddView):
    klass = StudyMediaTags
    field = 'media'


@login_required
def favorite(request, rid):
    UserResources(user=request.user, resource_id=rid).save()

    return redirect('resources_detail', rid)


@login_required
def unfavorite(request, rid):
    UserResources.objects.filter(user=request.user, resource_id=rid).delete()

    return redirect('resources_detail', rid)