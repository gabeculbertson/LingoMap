from django.db import models
from common.models import Tag
from django.core.urlresolvers import reverse


class Badge(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField(blank=True)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to='badges/%Y/%m/%d/', blank=True)
    tags = models.ManyToManyField(Tag, through='BadgeTags', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('badges_detail', args=[self.id])


class BadgeTags(models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    validity = models.FloatField(default=1.0)
