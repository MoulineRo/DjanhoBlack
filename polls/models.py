from django.db import models


class Teachers(models.Model):
    name = models.CharField(max_length=50)
