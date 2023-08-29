from envguardian import Env


class EmailConfig:
    EMAIL_HOST = Env.get('EMAIL_HOST')
    EMAIL_PORT = Env.get('EMAIL_PORT')
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = Env.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = Env.get('EMAIL_HOST_PASSWORD')
