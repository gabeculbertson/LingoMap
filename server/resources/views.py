from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from common.libs.models import RatingWidget

from .models import StudyMedia, StudyMediaTags, StudyMediaReview

from common.views import TagAddView, TagFlagView

from dashboard.models import UserResources


class StudyMediaForm(ModelForm):
    class Meta:
        model = StudyMedia
        fields = ['title', 'description', 'type', 'image', 'guide_text']


class StudyMediaReviewForm(ModelForm):
    class Meta:
        model = StudyMediaReview
        widgets = {
            'fun': RatingWidget,
            'useful': RatingWidget,
        }
        exclude = ['post', 'author']



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

    reviews = media.studymediareview_set.prefetch_related('author').all()

    added = False

    review_form = None

    if request.user.is_authenticated():
        try:
            UserResources.objects.get(user=request.user, resource=media)
            added = True
        except UserResources.DoesNotExist:
            pass

        review_form = StudyMediaReviewForm()

    return render(request, 'resources/detail.html', context={'m': media, 'added': added, 'reviews': reviews, 'review_form': review_form})


class MediaTagAddView(TagAddView):
    klass = StudyMediaTags
    field = 'media'


class MediaTagFlagView(TagFlagView):
    klass = StudyMediaTags
    field = 'media'


@login_required
@require_POST
def submit_review(request, rid):
    form = StudyMediaReviewForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.post_id = rid
        obj.author = request.user
        obj.save()

        return redirect('resources_detail', rid)
    else:
        raise Exception('Invalid form')

@login_required
def favorite(request, rid):
    UserResources(user=request.user, resource_id=rid).save()

    return redirect('resources_detail', rid)


@login_required
def unfavorite(request, rid):
    UserResources.objects.filter(user=request.user, resource_id=rid).delete()

    return redirect('resources_detail', rid)