"""
Add Environment variables here

Reference: https://pypi.org/project/validator/
"""

EnvironmentVariablesSchema = {
    "SECRET_KEY": "required|string",
    "DEBUG": "required|accepted",
    "TOKEN_LENGTH": "required|integer",
    "OTP_TOKEN_EXPIRES_IN_MINUTES": "required|integer",
    "DATABASE_NAME": "required|string",
    "DATABASE_USER": "required|string",
    "DATABASE_HOST": "required|string",
    "DATABASE_PORT": "required|integer",
}
