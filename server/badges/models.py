import random

from django.db import models
from common.models import Tag
from django.core.urlresolvers import reverse
from common.libs.models import BBCodeField


class Badge(models.Model):
    title = models.CharField(max_length=120)
    summary = BBCodeField(blank=True)
    detail = BBCodeField(blank=True)
    image = models.ImageField(upload_to='badges/%Y/%m/%d/', blank=True)
    tags = models.ManyToManyField(Tag, through='BadgeTags', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('badges_detail', args=[self.id])

    @property
    def visible_tags(self):
        return self.tags.filter(badgetags__validity__gte=random.random())


class BadgeTags(models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    validity = models.FloatField(default=1.0)
