from django.urls import path, include
from .views import InventoryViewset
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

app_name = "inventory"

router = DefaultRouter()
router.register("inventory", InventoryViewset, basename="inventory")

urlpatterns = [
    # url(r"^api/", include(router.urls)),
    path("api/", include(router.urls), name="api"),
]
