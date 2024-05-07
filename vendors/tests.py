from django.test import TestCase
from datetime import datetime
from .models import Vendor, PurchaseOrder
from django.utils import timezone

class VendorTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="Contact Details",
            address="Vendor Address",
            vendor_code="V001",
        )

    def test_update_performance_metrics_no_completed_orders(self):
        self.vendor.update_performance_metrics()
        self.assertIsNotNone(self.vendor.on_time_delivery_rate)
        self.assertIsNotNone(self.vendor.quality_rating_avg)
        self.assertIsNotNone(self.vendor.average_response_time)
        self.assertIsNotNone(self.vendor.fulfillment_rate)

    def test_update_performance_metrics_with_completed_orders(self):
        # Create completed orders for the vendor
        PurchaseOrder.objects.create(
            po_number="PO001",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items={},
            quantity=1,
            status="completed",
            quality_rating=4.5,
            issue_date=timezone.now(),
            acknowledgment_date=timezone.now(),
        )
        PurchaseOrder.objects.create(
            po_number="PO002",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items={},
            quantity=1,
            status="completed",
            quality_rating=3.5,
            issue_date=timezone.now(),
            acknowledgment_date=timezone.now(),
        )

        self.vendor.update_performance_metrics()
        self.assertIsNotNone(self.vendor.on_time_delivery_rate)
        self.assertIsNotNone(self.vendor.quality_rating_avg)
        self.assertIsNotNone(self.vendor.average_response_time)
        self.assertIsNotNone(self.vendor.fulfillment_rate)

    def test_update_performance_metrics_with_acknowledged_orders(self):
        # Create acknowledged orders for the vendor
        PurchaseOrder.objects.create(
            po_number="PO001",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items={},
            quantity=1,
            status="completed",
            quality_rating=4.5,
            issue_date=timezone.now(),
            acknowledgment_date=timezone.now(),
        )
        PurchaseOrder.objects.create(
            po_number="PO002",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items={},
            quantity=1,
            status="completed",
            quality_rating=3.5,
            issue_date=timezone.now(),
            acknowledgment_date=timezone.now(),
        )

        self.vendor.update_performance_metrics()
        self.assertIsNotNone(self.vendor.on_time_delivery_rate)
        self.assertIsNotNone(self.vendor.quality_rating_avg)
        self.assertIsNotNone(self.vendor.average_response_time)
        self.assertIsNotNone(self.vendor.fulfillment_rate)

    def test_update_performance_metrics_with_acknowledged_orders_and_response_time(self):
        # Create acknowledged orders for the vendor with response time
        PurchaseOrder.objects.create(
            po_number="PO001",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items={},
            quantity=1,
            status="completed",
            quality_rating=4.5,
            issue_date=timezone.now(),
            acknowledgment_date=timezone.now(),
        )
        PurchaseOrder.objects.create(
            po_number="PO002",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items={},
            quantity=1,
            status="completed",
            quality_rating=3.5,
            issue_date=timezone.now(),
            acknowledgment_date=timezone.now(),
        )

        self.vendor.update_performance_metrics()
        self.assertIsNotNone(self.vendor.on_time_delivery_rate)
        self.assertIsNotNone(self.vendor.quality_rating_avg)
        self.assertIsNotNone(self.vendor.average_response_time)
        self.assertIsNotNone(self.vendor.fulfillment_rate)

    def test_update_performance_metrics_with_acknowledged_orders_and_no_completed_orders(self):
        # Create acknowledged orders for the vendor without any completed orders
        PurchaseOrder.objects.create(
            po_number="PO001",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items={},
            quantity=1,
            status="pending",
            quality_rating=None,
            issue_date=timezone.now(),
            acknowledgment_date=timezone.now(),
        )
        PurchaseOrder.objects.create(
            po_number="PO002",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now(),
            items={},
            quantity=1,
            status="pending",
            quality_rating=None,
            issue_date=timezone.now(),
            acknowledgment_date=timezone.now(),
        )

        self.vendor.update_performance_metrics()
        self.assertIsNotNone(self.vendor.on_time_delivery_rate)
        self.assertIsNotNone(self.vendor.quality_rating_avg)
        self.assertIsNotNone(self.vendor.average_response_time)
        self.assertIsNotNone(self.vendor.fulfillment_rate)