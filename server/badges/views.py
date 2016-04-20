from django.shortcuts import render

from .models import Badge
from django import forms
from django.forms import ModelForm, Form
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404

from dashboard.models import UserResources


class BadgeForm(ModelForm):
    class Meta:
        model = Badge
        fields = ['title', 'summary', 'detail', 'image']


class BadgeCreateView(CreateView):
    form_class = BadgeForm
    template_name = 'badges/edit.html'


class BadgeUpdateView(UpdateView):
    form_class = BadgeForm
    model = Badge
    template_name = 'badges/edit.html'


class BadgeAddToMediaForm(Form):
    user_resource = forms.ModelChoiceField(queryset=UserResources.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(BadgeAddToMediaForm, self).__init__(*args, **kwargs)

        self.fields['user_resource'].queryset = UserResources.objects.filter(user=user)


def index(request):
    badges = Badge.objects.all()

    return render(request, 'badges/index.html', context={'badges': badges})


def detail(request, rid):
    badge = get_object_or_404(Badge, pk=rid)
    form = None
    if request.user.is_authenticated():
        form = BadgeAddToMediaForm(request.user)
    return render(request, 'badges/detail.html', context={'badge': badge, 'form': form})
