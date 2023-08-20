from django.conf import settings
from django.db import models


class Demo(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = settings.IS_TESTING
