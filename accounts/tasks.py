import logging
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import OtpCode

logger = logging.getLogger(__name__)

@shared_task
def delete_expired_otps():
    expiry_time = timezone.now() - timedelta(minutes=2)

    qs = OtpCode.objects.filter(created__lt=expiry_time)
    count = qs.count()
    qs.delete()

    logger.info(f"[OTP Task] Deleted {count} expired OTPs")
    return count
