from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView

from .models import StudyMedia


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
    return render(request, 'resources/detail.html', context={'m': media})
