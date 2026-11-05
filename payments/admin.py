from django.contrib import admin

from .models import ArticlePurchase, Payment, Subscription


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "purpose",
        "amount",
        "gateway",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "gateway",
        "purpose",
    )

    search_fields = (
        "user__username",
        "transaction_id",
        "provider_transaction_id",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "plan",
        "status",
        "starts_at",
        "ends_at",
    )

    list_filter = ("plan", "status")


@admin.register(ArticlePurchase)
class ArticlePurchaseAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "article_slug",
        "payment",
        "purchased_at",
    )
