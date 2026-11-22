from .models import ActivityLog


def log_activity(user, activity_type, description=""):
    ActivityLog.objects.create(
        user=user,
        activity_type=activity_type,
        description=description
    )