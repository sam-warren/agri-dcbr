from rest_framework import routers

from api import views

router = routers.SimpleRouter()

router.register(r"category", views.CategoryViewSet, "Category")
router.register(r"entry", views.EntryViewSet, "Entry")

urlpatterns = router.urls
