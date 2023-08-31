from typing import List, Dict, Any
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class MailClient:
    @staticmethod
    def send_email(subject: str, message: str, from_email: str, recipients: List[str],
                   html_message: str = None):  # type: ignore # noqa: ignore
        return send_mail(subject, message, from_email, recipient_list=recipients, html_message=html_message)

    @staticmethod
    def send_html_email(subject: str, from_email: str, recipients: List[str], html_template: str,
                        context: Dict[str, Any]):
        html_message = render_to_string(html_template, context)

        return MailClient.send_email(subject, strip_tags(html_message), from_email, recipients, html_message)

    @staticmethod
    def send_welcome_email(email: str, first_name: str, token: str):
        return MailClient.send_html_email("Welcome to Realty With Ease", 'tech@realtywithease.come', [email],
                                          'user_management/emails/welcome_mail.html',
                                          {"first_name": first_name, "token": token})
