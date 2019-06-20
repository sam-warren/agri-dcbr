import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def authenticate(request):
    return render(request, "authenticate.html")


def public_sso_config(request):

    return JsonResponse(
        {
            "KEYCLOAK_PUBLIC_AUTH_URL": settings.KEYCLOAK_PUBLIC_AUTH_URL,
            "KEYCLOAK_PUBLIC_CLIENT_ID": settings.KEYCLOAK_PUBLIC_CLIENT_ID,
            "KEYCLOAK_PUBLIC_REALM": settings.KEYCLOAK_PUBLIC_REALM,
        }
    )
