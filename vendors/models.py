from django.db import models
from django.db.models import Avg, F


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def update_performance_metrics(self):
        completed_orders = PurchaseOrder.objects.filter(vendor=self, status="completed")
        self.on_time_delivery_rate = (
            completed_orders.filter(delivery_date__lte=F("order_date")).count()
            / completed_orders.count()
            if completed_orders.exists()
            else 0
        )
        self.quality_rating_avg = (
            completed_orders.aggregate(Avg("quality_rating"))["quality_rating__avg"]
            or 0.0
        )
        acknowledged_orders = PurchaseOrder.objects.filter(vendor=self).exclude(
            acknowledgment_date=None
        )
        total_response_time = sum(
            [
                (po.acknowledgment_date - po.issue_date).total_seconds()
                for po in acknowledged_orders
            ]
        )
        self.average_response_time = (
            total_response_time / acknowledged_orders.count()
            if acknowledged_orders.exists()
            else 0
        )
        self.fulfillment_rate = (
            completed_orders.filter(quality_rating__isnull=False).count()
            / completed_orders.count()
            if completed_orders.exists()
            else 0
        )
        self.save()


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.vendor.update_performance_metrics()


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
