from django.db import models
from django.contrib.auth.models import User

from common.models import Tag
from resources.models import StudyMedia
from badges.models import Badge


class UserFavoriteTags(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'tag')


class UserResources(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(StudyMedia, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.resource)

    class Meta:
        unique_together = ('user', 'resource')


class AssignedBadges(models.Model):
    resource = models.ForeignKey(UserResources, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    completed = models.BooleanField()
    completed_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('badge', 'resource')


