from config.business_config import BusinessConfig
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.infrastructure.internal import JwtClient
from core.system_messages import (
    STATUS_CODE,
    STATUS,
    ERROR,
    MESSAGE,
    RESULTS,
    VALIDATION_ERROR,
    SUCCESS,
    OPERATION_SUCCESSFUL,
    SOMETHING_WENT_WRONG,
)
from user_management.models import User
from user_management.models.user_profile import UserProfile
from user_management.serializers.authentication_serializers import (
    AuthenticateUserRequestSerializer,
)


@api_view(["POST"])
def authenticate_user(request):
    try:
        serializer = AuthenticateUserRequestSerializer(data=request.data)

        if serializer.is_valid():
            email = request.data.get("email")
            password = request.data.get("password")

            user = User.objects.filter(email=email).first()

            is_password_valid = user.check_password(password)

            if not is_password_valid:
                print('password is invalid')
                return Response(
                    {
                        STATUS_CODE: status.HTTP_400_BAD_REQUEST,
                        STATUS: ERROR,
                        MESSAGE: "Invalid Credentials",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            access_token = JwtClient.encode({"email": user.email})

            user_profile = UserProfile.objects.filter(user=user).first()

            user.last_login = BusinessConfig.get_current_date_time()
            user.save()

            return Response(
                {
                    STATUS_CODE: status.HTTP_200_OK,
                    STATUS: SUCCESS,
                    MESSAGE: OPERATION_SUCCESSFUL("Authenticate User"),
                    RESULTS: {
                        **user.for_client(),
                        **user_profile.for_client(),
                        "access_credentials": {"token": access_token},
                    },
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                STATUS_CODE: status.HTTP_400_BAD_REQUEST,
                STATUS: ERROR,
                MESSAGE: VALIDATION_ERROR,
                RESULTS: serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        print("🧨 -> user_management.authenticate_user_error:", e)

        return Response(
            {
                STATUS_CODE: status.HTTP_500_INTERNAL_SERVER_ERROR,
                STATUS: ERROR,
                MESSAGE: SOMETHING_WENT_WRONG,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
