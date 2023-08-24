from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from core.infrastructure.internal import JwtClient
from core.system_messages import ERROR, UNAUTHENTICATED_ERROR, STATUS_CODE, STATUS, MESSAGE
from user_management.models import User


def jwt_required(view_func):
    """
    This is the decorator that checks if a valid JWT is available in the request headers
    :param view_func:
    :return:
    """

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        authorization = request.META.get("Authorization") or request.META.get('HTTP_AUTHORIZATION')

        if authorization is None:
            return Response({
                STATUS_CODE: status.HTTP_401_UNAUTHORIZED,
                STATUS: ERROR,
                MESSAGE: UNAUTHENTICATED_ERROR}, status=status.HTTP_401_UNAUTHORIZED)

        token = authorization.replace("Bearer ", "")

        decoded_jwt = JwtClient.decode(token)

        if decoded_jwt is None:
            return Response({
                STATUS_CODE: status.HTTP_401_UNAUTHORIZED,
                STATUS: ERROR,
                MESSAGE: UNAUTHENTICATED_ERROR}, status=status.HTTP_401_UNAUTHORIZED)

        user_email = decoded_jwt.get('email')

        if user_email is None:
            return Response({
                STATUS_CODE: status.HTTP_401_UNAUTHORIZED,
                STATUS: ERROR,
                MESSAGE: UNAUTHENTICATED_ERROR}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.filter(email=user_email).first()

        if user is None:
            return Response({
                STATUS_CODE: status.HTTP_401_UNAUTHORIZED,
                STATUS: ERROR,
                MESSAGE: UNAUTHENTICATED_ERROR}, status=status.HTTP_401_UNAUTHORIZED)

        request.user = user

        # Call the original view function
        response = view_func(request, *args, **kwargs)
        return response

    return wrapper
