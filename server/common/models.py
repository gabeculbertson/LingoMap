from django.db import models

TAG_ADD_VALIDITY_BOOST = 1.2
TAG_FLAG_VALIDITY_DAMP = 0.9


class Tag(models.Model):
    tag = models.CharField(max_length=40)