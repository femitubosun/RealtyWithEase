from typing import List
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class MailClient:
    @staticmethod
    def send_email(subject: str, message: str, from_email: str, recipients: List[str],
                   html_message: str = None):  # type: ignore # noqa: ignore
        return send_mail(subject, message, from_email, recipient_list=recipients, html_message=html_message)

    @staticmethod
    def send_welcome_email(email: str, first_name: str, token: str):
        welcome_email_template = 'user_management/emails/welcome_mail.html'

        html_message = render_to_string(welcome_email_template, {"first_name": first_name, "token": token})

        return MailClient.send_email("Welcome To Realty With Ease", strip_tags(html_message), 'tech@realtywithease.com',
                                     [email],
                                     html_message)
