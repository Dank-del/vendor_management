from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorPerformanceView, VendorViewSet, PurchaseOrderViewSet

router = DefaultRouter()
router.register(r"vendors", VendorViewSet)
router.register(r"purchase_orders", PurchaseOrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api/vendors/<int:vendor_id>/performance/",
        VendorPerformanceView.as_view(),
        name="vendor-performance",
    ),
]
