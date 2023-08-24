from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.decorators.jwt_required import jwt_required
from core.system_messages import (
    STATUS_CODE,
    STATUS,
    SUCCESS,
    OPERATION_SUCCESSFUL,
    RESULTS,
    MESSAGE,
    ERROR,
    SOMETHING_WENT_WRONG,
)
from user_management.models import UserProfile


@api_view(["GET"])
@jwt_required
def get_user_profile(request):
    try:
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()

        return Response(
            {
                STATUS_CODE: status.HTTP_200_OK,
                STATUS: SUCCESS,
                MESSAGE: OPERATION_SUCCESSFUL("Fetch User Profile"),
                RESULTS: {
                    **user.for_client(),
                    **user_profile.for_client(),
                },
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print("🧨 -> user_management.get_user_profile:", e)

        return Response(
            {
                STATUS_CODE: status.HTTP_500_INTERNAL_SERVER_ERROR,
                STATUS: ERROR,
                MESSAGE: SOMETHING_WENT_WRONG,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
