import os


class BusinessConfig:
    DEBUG = os.getenv("DEBUG")
    SECRET = os.getenv("SECRET_KEY")
