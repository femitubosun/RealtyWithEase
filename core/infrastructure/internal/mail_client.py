from typing import List
from django.core.mail import send_mail


class MailClient:
    @staticmethod
    def send_email(subject: str, message: str, from_email: str, recipients: List[str]):
        return send_mail(subject, message, from_email, recipient_list=recipients)

    @staticmethod
    def send_welcome_email(email: str, token: str):
        print(token)
        return MailClient.send_email("Welcome To Realty With Ease", 'Welcome', 'tech@realtywithease.com', [email])
