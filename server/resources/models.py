import random

from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

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

LEVELS = (
    (-1, 'No one'),
    (0, 'Anyone'),
    (1, 'Beginner'),
    (2, 'Intermediate'),
    (3, 'Advanced'),
)

CHALLENGING = (
    (1, 'Too easy'),
    (2, 'Just right'),
    (3, 'Too hard'),
)


class StudyMediaReview(models.Model):
    post = models.ForeignKey(StudyMedia)
    author = models.ForeignKey(User)
    recommend = models.BooleanField()
    fun = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    useful = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    level = models.IntegerField(choices=LEVELS)
    challenging = models.IntegerField(choices=CHALLENGING)
    comment = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('resources_detail', args=[self.post_id])
