from django.core.management.base import BaseCommand
from faker import Faker

from polls.models import Teachers


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("questions", type=int)

    def handle(
            self,
            *args,
            questions,
            **options,
    ):
        fake = Faker()
        fake.name()
        for _ in range(questions):
            q = Teachers.objects.create(name=fake.name())
            self.stdout.write(
                self.style.SUCCESS('Successfully created Question with ID "%s"' % q.id)
            )
