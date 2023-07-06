import os
from datetime import datetime
from django.utils import timezone


class OtpTokenConfig:
    """
    Otp Token Configuration
    """

    LENGTH = int(os.getenv("TOKEN_LENGTH") or "6")
    EXPIRES_IN_MINUTES = int(os.getenv("OTP_TOKEN_EXPIRES_IN_MINUTES") or "10")


class BusinessConfig:
    DEBUG = os.getenv("DEBUG")
    SECRET = os.getenv("SECRET_KEY")

    OTP_TOKEN = OtpTokenConfig

    @staticmethod
    def get_current_date_time():
        return datetime.now().replace(tzinfo=timezone.get_current_timezone())
