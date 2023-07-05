from django.db import models
from common.models import BaseModel
from config import BusinessConfig
from common.utils import generate_future_date_time


class OtpToken(BaseModel):
    """
    This Model defines an OTP Token Information
    """

    TOKEN_TYPES = [
        ("reset-password", "reset-password"),
        ("login", "login"),
        ("email", "email"),
    ]

    email = models.EmailField()
    token = models.CharField(max_length=BusinessConfig.OTP_TOKEN.LENGTH)
    type = models.CharField(choices=TOKEN_TYPES, max_length=14)
    is_revoked = models.BooleanField(default=False)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Add expiration time before saving
        self.expires_at = self.expires_at = generate_future_date_time(
            BusinessConfig.OTP_TOKEN.EXPIRES_IN_MINUTES
        )

        super().save(*args, **kwargs)

    def __repr__(self):
        return f"<Otp Token: {self.email}-{self.type}>"

    def __str__(self):
        return f"<Otp Token: {self.email}-{self.type}>"
