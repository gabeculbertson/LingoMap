import random

from django.db import models
from django.core.urlresolvers import reverse

from common.models import Tag
from common.libs.models import BBCodeField


class StudyMediaType(models.Model):
    category = models.CharField(max_length=40)
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.category + " - " + self.type


class StudyMedia(models.Model):
    title = models.CharField(max_length=120)
    description = BBCodeField(blank=True)
    type = models.ForeignKey(StudyMediaType, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True, through='StudyMediaTags')
    image = models.ImageField(upload_to='resources/%Y/%m/%d/')
    guide_text = BBCodeField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resources_detail', args=[self.id])

    @property
    def visible_tags(self):
        return self.tags.filter(studymediatags__validity__gte=random.random())

    @property
    def rating(self):
        return hash(self.title) % 5 + 1

    @property
    def has_rating(self):
        return hash(self.title) % 10 < 8


class StudyMediaTags(models.Model):
    media = models.ForeignKey(StudyMedia, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    validity = models.FloatField(default=1.0)
