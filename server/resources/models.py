from django.db import models
from django.core.urlresolvers import reverse

from common.models import Tag


class StudyMediaType(models.Model):
    category = models.CharField(max_length=40)
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.category + " - " + self.type


class StudyMedia(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    type = models.ForeignKey(StudyMediaType, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='resources/%Y/%m/%d/')
    guide_text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resources_detail', args=[self.id])

    @property
    def rating(self):
        return hash(self.title) % 5 + 1

    @property
    def has_rating(self):
        return hash(self.title) % 10 < 8
