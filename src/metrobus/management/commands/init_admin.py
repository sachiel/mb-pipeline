# BASED: https://github.com/dkarchmer/aws-eb-docker-django/blob/master/authentication/management/commands/initadmin.py

from django.conf import settings
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superadmin in project. user:admin, pass:1q2w3e4r'

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for user in settings.ADMINS:
                username = 'admin'
                email = user[1]
                password = '1q2w3e4r'
                print('Creating account for %s (%s)' % (username, email))
                admin = User.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')

