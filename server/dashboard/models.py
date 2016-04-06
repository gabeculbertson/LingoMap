from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


class Goal(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
