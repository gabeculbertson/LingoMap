from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.generic import View

from .models import Tag, TAG_ADD_VALIDITY_BOOST


class TagAddView(View):
    klass = None
    field = ''

    def post(self, request):
        tag, created = Tag.objects.get_or_create(tag=request.POST.get('tag'))

        attrs = {
            'tag': tag,
            self.field + '_id': int(request.POST.get('id'))
        }
        relation, created = self.klass.objects.get_or_create(**attrs)
        if not created:
            relation.validity = max(relation.validity * TAG_ADD_VALIDITY_BOOST, 1.0)
            relation.save()

        return redirect(request.POST.get('next'))


def tags_list(request):
    tag_objects = Tag.objects.filter(tag__icontains=request.GET.get('term', ''))[:50]
    response = [tag.tag for tag in tag_objects]

    return JsonResponse(response, safe=False)
