# import logging

# from django.conf import settings
# from django.db import connection
# from django.http import JsonResponse
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework import permissions
# from rest_framework.decorators import (api_view, authentication_classes,
#                                        parser_classes, permission_classes)
# from rest_framework.parsers import FormParser

# LOGGER = logging.getLogger(__name__)

# @api_view(["POST"])
# @authentication_classes(())
# @permission_classes((permissions.AllowAny,))
# @parser_classes((FormParser,))
# def send_feedback(request, *args, **kwargs):
#     x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
#     if x_forwarded_for:
#         ip_addr = x_forwarded_for.split(",")[0]
#     else:
#         ip_addr = request.META.get("REMOTE_ADDR")
#     from_name = request.POST.get("from_name")
#     from_email = request.POST.get("from_email")
#     reason = request.POST.get("reason")
#     comments = request.POST.get("comments")
#     email_feedback(ip_addr, from_name, from_email, reason, comments)
#     return JsonResponse({"status": "ok"})
