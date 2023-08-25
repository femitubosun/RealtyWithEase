from django.db import models
from core.models import BaseModel
from config import BusinessConfig
from core.utils import generate_future_date_time, generate_random_string
from datetime import datetime,timedelta



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
            minutes=BusinessConfig.OTP_TOKEN.EXPIRES_IN_MINUTES
        )

        super().save(*args, **kwargs)

    def __repr__(self):
        return f"<Otp Token: {self.email}-{self.type}>"

    def __str__(self):
        return f"<Otp Token: {self.email}-{self.type}>"
    
    @staticmethod
    def generate_otp_token():
        return generate_random_string(BusinessConfig.TOKEN_LENGTH, True, 'alphanumeric')
        
 
    @staticmethod
    def generate_otp_token_expiration_time(valid_minutes):
        current_time = BusinessConfig.get_current_date_time()
        return current_time + timedelta(minutes=valid_minutes)
        
    

        