from typing import Dict, Any, Optional
from datetime import timedelta

import jwt
from config import BusinessConfig


class JwtClient:
    """
    This class represents the JWT Client to be used for encoding and decoding Json Web Tokens
    """

    @staticmethod
    def encode(payload: Optional[Dict[str, Any]] = None) -> str:
        if payload is None:
            payload = {}

        payload['exp'] = BusinessConfig.get_current_date_time() + timedelta(
            minutes=BusinessConfig.JWT.EXPIRES_IN_MINUTES)

        return jwt.encode(payload, BusinessConfig.SECRET, algorithm="HS256")

    @staticmethod
    def decode(jwt_string: str):
        try:
            return jwt.decode(jwt_string, BusinessConfig.SECRET, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return None
