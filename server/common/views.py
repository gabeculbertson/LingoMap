from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.generic import View

from .models import Tag, TAG_ADD_VALIDITY_BOOST, TAG_FLAG_VALIDITY_DAMP


class TagAddView(View):
    klass = None
    field = ''

    def post(self, request):
        tag_name = request.POST.get('tag')
        if len(tag_name) > 0:
            tag, created = Tag.objects.get_or_create(tag=tag_name)

            attrs = {
                'tag': tag,
                self.field + '_id': int(request.POST.get('id'))
            }
            relation, created = self.klass.objects.get_or_create(**attrs)
            if not created:
                relation.validity = max(relation.validity * TAG_ADD_VALIDITY_BOOST, 1.0)
                relation.save()

        return redirect(request.POST.get('next'))


class TagFlagView(View):
    klass = None
    field = ''

    def get(self, request):
        tag_id = int(request.GET.get('tag_id'))

        attrs = {
            'tag_id': tag_id,
            self.field + '_id': int(request.GET.get('id'))
        }
        relation = self.klass.objects.get(**attrs)
        relation.validity = relation.validity * TAG_FLAG_VALIDITY_DAMP
        relation.save()

        return JsonResponse({'success': True})


def tags_list(request):
    tag_objects = Tag.objects.filter(tag__icontains=request.GET.get('term', ''))[:50]
    response = [tag.tag for tag in tag_objects]

    return JsonResponse(response, safe=False)
