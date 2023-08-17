from datetime import datetime
from django.utils import timezone
from envguardian import Env


class OtpTokenConfig:
    """
    Otp Token Configuration
    """

    LENGTH = Env.get('TOKEN_LENGTH')
    EXPIRES_IN_MINUTES = Env.get('OTP_TOKEN_EXPIRES_IN_MINUTES')


class JwtConfig:
    EXPIRES_IN_MINUTES = Env.get('JWT_TOKEN_EXPIRES_IN_MINUTES')


class BusinessConfig:
    DEBUG = Env.get('DEBUG')
    SECRET = Env.get('SECRET_KEY')

    OTP_TOKEN = OtpTokenConfig

    JWT = JwtConfig

    @staticmethod
    def get_current_date_time():
        return datetime.now().replace(tzinfo=timezone.get_current_timezone())
