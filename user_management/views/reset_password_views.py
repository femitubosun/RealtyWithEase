import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_management.models import OtpToken
from user_management.models import User
from core.infrastructure.internal import MailClient
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import password_validation


from core.system_messages import (
    STATUS_CODE,
    STATUS,
    ERROR,
    MESSAGE,
    RESULTS,
    SOMETHING_WENT_WRONG,
)


@api_view(['POST'])
def send_reset_otp_email(request):
    email = request.data.get('email')
    
    #To validate email.
    try:
        validate_email(email)
    except ValidationError:
        return Response({"message": "Email is required in the request."}, status=status.HTTP_400_BAD_REQUEST)
    
    #To confirm is user's account exist.
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
    email = request.data.get("email")
    otp = request.data.get("otp")
    new_password = request.data.get("new_password")
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response(
            {
                STATUS: status.HTTP_404_NOT_FOUND,
                MESSAGE: "User not found",
            }
        )
    
    try:
        otp_token = OtpToken.objects.get(user=user, token=otp)
    except OtpToken.DoesNotExist:
        return Response(
            {
                STATUS: status.HTTP_400_BAD_REQUEST,
                MESSAGE:"Invalid OTP token",    
            }
        )
    
    try:
        validate_password(new_password, user=user, password_validators=password_validation.get_default_password_validators())
    except ValidationError as VALIDATION_ERROR :
        return Response(
            {
                STATUS_CODE: status.HTTP_400_BAD_REQUEST,
                MESSAGE: VALIDATION_ERROR,
            }
        )

    user.set_password(new_password)
    user.save()
    otp_token.delete()
    
    return Response({'message': 'Password reset successfully'})
