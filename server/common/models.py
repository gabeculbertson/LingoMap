from django.db import models

TAG_ADD_VALIDITY_BOOST = 1.2


class Tag(models.Model):
    tag = models.CharField(max_length=40)