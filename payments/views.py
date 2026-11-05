from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Payment


def plans(request):

    plans = [
        {
            "name": "Free",
            "price": 0,
            "period": "Forever",
            "features": [
                "Read regular news",
                "Browse news categories",
                "Create an account",
            ],
        },
        {
            "name": "Monthly",
            "price": 300,
            "period": "Month",
            "features": [
                "Everything in Free",
                "Read premium articles",
                "Access exclusive news",
            ],
        },
        {
            "name": "Yearly",
            "price": 3000,
            "period": "Year",
            "features": [
                "Everything in Free",
                "Read premium articles",
                "Access exclusive news",
                "Save money annually",
            ],
        },
    ]

    return render(request, "payments/plans.html", {"plans": plans})


@login_required
def payment_history(request):

    payments = Payment.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "payments/history.html", {"payments": payments})


def payment_success(request):
    return render(request, "payments/success.html")


def payment_cancel(request):
    return render(request, "payments/cancel.html")
