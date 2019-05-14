import os
from django.contrib.auth.models import User, Group

ADMIN_NAME = os.getenv("DJANGO_ADMIN_USER")
ADMIN_PASSWORD = os.getenv("DJANGO_ADMIN_PASSWORD")
ADMIN_EMAIL = os.getenv("DJANGO_ADMIN_EMAIL")

superuser = None

try:
    superuser = User.objects.get(username=ADMIN_NAME)
except Exception:
    print("***** No superuser was detected, creating new...")
    User.objects.create_superuser(ADMIN_NAME, ADMIN_EMAIL, ADMIN_PASSWORD)
    print("***** New superuser '{}' created successfully!".format(ADMIN_NAME))
