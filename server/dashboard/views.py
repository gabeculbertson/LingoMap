from collections import OrderedDict

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.humanize.templatetags.humanize import naturalday

from .models import UserFavoriteTags, UserResources, AssignedBadges


@login_required
def index(request):
    user = request.user
    context = {}
    fav_tags = [f.tag for f in UserFavoriteTags.objects.select_related('tag').filter(user=user)]
    context['fav_tags'] = fav_tags

    resources = UserResources.objects.select_related('resource').filter(user=user)
    context['resources'] = resources

    assigned_badges = AssignedBadges.objects.select_related('badge')\
                                    .filter(completed=True, resource__user=user).order_by('-completed_at')

    history = OrderedDict()
    for ab in assigned_badges:
        day = naturalday(ab.completed_at)
        if day not in history:
            history[day] = []

        history[day].append(ab.badge)

    context['history'] = history

    return render(request, 'dashboard/index.html', context=context)


@login_required
def badge_mark_complete(request, pk):
    AssignedBadges.objects.filter(id=pk, resource__user_id=request.user.id).update(completed=True)

    return redirect('dashboard_index')


@login_required
def badge_mark_uncomplete(request, pk):
    AssignedBadges.objects.filter(id=pk, resource__user_id=request.user.id).update(completed=False)

    return redirect('dashboard_index')
