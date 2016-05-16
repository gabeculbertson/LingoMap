from django.shortcuts import render, redirect

from .models import Badge, BadgeTags
from django import forms
from django.forms import ModelForm, Form
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404

from dashboard.models import UserResources, AssignedBadges
from common.views import TagAddView, TagFlagView


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

    def __init__(self, user, badge_id, *args, **kwargs):
        super(BadgeAddToMediaForm, self).__init__(*args, **kwargs)

        self.fields['user_resource'].queryset = UserResources.objects.filter(user=user).exclude(assignedbadges__badge_id=badge_id)


class BadgeTagAddView(TagAddView):
    klass = BadgeTags
    field = 'badge'


class BadgeTagFlagView(TagFlagView):
    klass = BadgeTags
    field = 'badge'


def index(request):
    badges = Badge.objects.all()

    return render(request, 'badges/index.html', context={'badges': badges})


def detail(request, rid):
    badge = get_object_or_404(Badge, pk=rid)
    form = None
    if request.user.is_authenticated():
        form = BadgeAddToMediaForm(request.user, int(rid))
    return render(request, 'badges/detail.html', context={'badge': badge, 'form': form})


def addto(request, pk):
    assignment = AssignedBadges()
    assignment.resource_id = int(request.POST.get('user_resource'))
    assignment.badge_id = int(pk)
    assignment.completed = False
    assignment.save()

    return redirect('badges_detail', pk)