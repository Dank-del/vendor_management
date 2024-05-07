from rest_framework import viewsets, status
from .models import Vendor, PurchaseOrder
from .serializers import (
    VendorSerializer,
    PurchaseOrderSerializer,
    VendorPerformanceSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class VendorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        vendor_id = self.request.query_params.get("vendor_id")
        if vendor_id is not None:
            return self.queryset.filter(vendor_id=vendor_id)
        return self.queryset


class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response(
                {"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Serialize vendor performance data
        serializer = VendorPerformanceSerializer(vendor)
        return Response(serializer.data)
