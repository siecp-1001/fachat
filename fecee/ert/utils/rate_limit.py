from django.utils import timezone
from ert.models import Conversation

def check_rate_limit(user):
    last = Conversation.objects.filter(user=user).order_by("-timestamp").first()
    if not last:
        return True

    delta = timezone.now() - last.timestamp
    return delta.total_seconds() > 1  # 1 second cooldown
