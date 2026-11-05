from django.urls import path

from . import views

app_name = "payments"

urlpatterns = [
    path("plans/", views.plans, name="plans"),
    path("history/", views.payment_history, name="history"),
    path("success/", views.payment_success, name="success"),
    path("cancel/", views.payment_cancel, name="cancel"),
]
