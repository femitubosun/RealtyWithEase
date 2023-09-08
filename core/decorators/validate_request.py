from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from core.system_messages import STATUS_CODE, STATUS, ERROR, MESSAGE, VALIDATION_ERROR, RESULTS


def validate_request(validation_schema):
    """
    This is the decorator that validates the request body against a validation_schema
    :param validation_schema:
    :return:
    """

    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            serializer = validation_schema(data=request.data)

            if not serializer.is_valid():
                return Response(
                    {
                        STATUS_CODE: status.HTTP_400_BAD_REQUEST,
                        STATUS: ERROR,
                        MESSAGE: VALIDATION_ERROR,
                        RESULTS: serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return view_func(request, *args, **kwargs)

        return wrapped_view

    return decorator
