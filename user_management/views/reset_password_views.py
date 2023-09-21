import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_management.models import OtpToken
from user_management.models import User
from core.infrastructure.internal import JwtClient, MailClient
import random

from core.system_messages import (
    STATUS_CODE,
    STATUS,
    ERROR,
    MESSAGE,
    SOMETHING_WENT_WRONG,
)


@api_view(['POST'])
def send_reset_otp_email(request):
    email = request.data.get('email')
    # TO confirm is user's account exist.
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    
    otp_token = ''.join(random.choice('0123456789') for _ in range(6))
    OtpToken.objects.update_or_create(user=user, defaults={"token": otp_token})
    
    subject = "Password Reset OTP"
    message = f"Hi, Use the OTP code token to complete password reset on your Realty With Ease account: {otp_token}"
    sender_mail = "realtywitheasepy@gmail.com"
    recipient_list = [email]
    
    try:
        MailClient.send_email(subject, message, sender_mail, recipient_list) 
    except Exception as e:
        return Response(
            {
                STATUS_CODE: status.HTTP_500_INTERNAL_SERVER_ERROR,
                STATUS: ERROR,
                MESSAGE: SOMETHING_WENT_WRONG,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
    return Response({"message": " OTP successfully sent "})


@api_view(['POST'])
def  reset_password(request):
    email = request.data.get('email')
    