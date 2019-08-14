from django.conf import settings
from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

API_METADATA = settings.API_METADATA
schema_view = get_schema_view(
    openapi.Info(
        title=API_METADATA["title"],
        default_version="v1",
        description=API_METADATA["description"],
        terms_of_service=API_METADATA["terms"]["url"],
        contact=openapi.Contact(**API_METADATA["contact"]),
        license=openapi.License(**API_METADATA["license"]),
    ),
    validators=["ssv"],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()

router.register(r"registration", views.Registration_ViewSet, "Registration")
router.register(r"operator", views.Operator_ViewSet, "Operator")
router.register(r"address", views.Address_ViewSet, "Address")
router.register(r"inspection", views.Inspection_ViewSet, "Inspection")
router.register(
    r"riskoperations", views.Risk_Factor_Operation_ViewSet, "RiskOperations"
)
router.register(r"riskanimals", views.Risk_Factor_Animal_ViewSet, "RiskAnimals")
router.register(r"association", views.Association_ViewSet, "Association")

# fmt: off
swaggerpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=None), name="api-docs"),
]
# fmt: on

# urlpatterns = [format_suffix_patterns(router.urls + swaggerpatterns)
#                 # path(r'^__debug__, include(debug_toolbar.urls')
# ]
urlpatterns = format_suffix_patterns(router.urls + swaggerpatterns)
