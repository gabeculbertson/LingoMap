from django.http import JsonResponse

from .models import Tag


def tags_list(request):
    tag_objects = Tag.objects.filter(tag__icontains=request.GET.get('term', ''))[:50]
    response = [tag.tag for tag in tag_objects]

    return JsonResponse(response, safe=False)
