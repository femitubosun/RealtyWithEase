from envguardian import Env


class EmailConfig:
    """
    Email Configuration Values
    """
    SMTP_HOST = Env.get('SMTP_HOST')
    SMTP_PORT = Env.get('SMTP_PORT')
    SMTP_USER = Env.get('SMTP_USER')
    SMTP_PASSWORD = Env.get('SMTP_PASSWORD')
