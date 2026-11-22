from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from django.dispatch import receiver

from .utils import log_activity


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    log_activity(
        user,
        "login",
        "User logged in successfully."
    )


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    if user:
        log_activity(
            user,
            "logout",
            "User logged out."
        )


@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    log_activity(
        None,
        "failed_login",
        "A failed login attempt occurred."
    )