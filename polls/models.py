from django.db import models
from faker import Faker


fake = Faker()
fake.name()


class Teachers(models.Model):
    name = models.CharField(max_length=50)

for _ in range(20):
    s = Teachers.objects.create(name=fake.name())