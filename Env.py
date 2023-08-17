"""
Add Environment variables here

Reference: https://pypi.org/project/envguardian/
"""
from envguardian import Env

env_schema = {
    "SECRET_KEY": Env.string(),
    "DEBUG": Env.boolean(),
    "TOKEN_LENGTH": Env.integer(),
    "OTP_TOKEN_EXPIRES_IN_MINUTES": Env.integer(),
    "JWT_TOKEN_EXPIRES_IN_MINUTES": Env.integer(),

    'DATABASE_NAME': Env.string(),
    'DATABASE_USER': Env.string(),
    "DATABASE_PASSWORD": Env.string(),
    'DATABASE_PORT': Env.integer(),
    'DATABASE_HOST': Env.string(),

}
