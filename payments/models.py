import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone


class Payment(models.Model):

    PURPOSE_CHOICES = [
        ("subscription", "Subscription"),
        ("article", "Article Purchase"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
        ("cancelled", "Cancelled"),
    ]

    GATEWAY_CHOICES = [
        ("bkash", "bKash"),
        ("sslcommerz", "SSLCOMMERZ"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments"
    )

    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    currency = models.CharField(max_length=3, default="BDT")

    gateway = models.CharField(max_length=20, choices=GATEWAY_CHOICES)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    provider_transaction_id = models.CharField(max_length=100, blank=True)

    article_slug = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - " f"{self.amount} BDT - {self.status}"


class Subscription(models.Model):

    PLAN_CHOICES = [
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    ]

    STATUS_CHOICES = [
        ("active", "Active"),
        ("expired", "Expired"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscriptions"
    )

    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")

    starts_at = models.DateTimeField(default=timezone.now)

    ends_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def is_active(self):
        now = timezone.now()

        return self.status == "active" and self.starts_at <= now and self.ends_at > now

    def __str__(self):
        return f"{self.user.username} - {self.plan}"


class ArticlePurchase(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="article_purchases",
    )

    article_slug = models.CharField(max_length=200)

    payment = models.OneToOneField(
        Payment, on_delete=models.PROTECT, related_name="article_purchase"
    )

    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "article_slug"], name="unique_user_article_purchase"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.article_slug}"
