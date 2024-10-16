import os

from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv("EMAIL_CSU"),
            first_name=os.getenv("NAME_CSU"),
            last_name=os.getenv("LAST_NAME_CSU"),
            phone='5461611',
            password=os.getenv("PASSWORD_CSU"),
            role="admin"
        )
        user.is_active = True
        user.set_password(os.getenv("PASSWORD_CSU"))
        user.save()