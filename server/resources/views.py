from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm

from .models import StudyMedia


class StudyMediaForm(ModelForm):
    class Meta:
        model = StudyMedia
        fields = ['title', 'description', 'type', 'image', 'guide_text']


def index(request):
    media = StudyMedia.objects.all()

    return render(request, 'resources/index.html', context={'media': media})


def detail(request, rid):
    media = get_object_or_404(StudyMedia, pk=rid)
    return render(request, 'resources/detail.html', context={'m': media})


def addedit_media(request, form, editing=False):
    return render(request, 'resources/edit.html', context={'form': form})


def add_media(request):
    return addedit_media(request, StudyMediaForm(), editing=False)


def edit_media(request, rid):
    media = get_object_or_404(StudyMedia, pk=rid)
    return addedit_media(request, StudyMediaForm(instance=media), editing=True)