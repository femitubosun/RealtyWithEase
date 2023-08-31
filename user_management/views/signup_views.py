from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from config import BusinessConfig
from core.infrastructure.internal import JwtClient, MailClient
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
from user_management.models import User, UserProfile, OtpToken
from user_management.serializers import (
    SignupTenantRequestSerializer,
    SignupLandlordRequestSerializer,
    SignupAgentRequestSerializer,
)


@api_view(["POST"])
def sign_up_as_tenant(request):
    try:
        serializer = SignupTenantRequestSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            first_name = serializer.validated_data.get("first_name")
            last_name = serializer.validated_data.get("last_name")
            password = serializer.validated_data.get("password")
            gender = serializer.validated_data.get("gender")

            created_user = User.objects.create_user(
                email, password, first_name=first_name, last_name=last_name
            )
            user_profile = UserProfile.objects.create(
                user=created_user, gender=gender, is_tenant=True
            )

            access_token = JwtClient.encode({"email": created_user.email})

            created_user.last_login = BusinessConfig.get_current_date_time()

            created_user.save()

            token = OtpToken.generate_otp_token()

            OtpToken.objects.create(email=created_user.email, token=token, type="email",
                                    expires_at=OtpToken.generate_otp_token_expiration_time())

            MailClient.send_welcome_email(email=created_user.email, first_name=first_name, token=token)

            return Response(
                {
                    STATUS_CODE: status.HTTP_201_CREATED,
                    STATUS: SUCCESS,
                    MESSAGE: OPERATION_SUCCESSFUL("Signup Tenant User"),
                    RESULTS: {
                        **created_user.for_client(),
                        **user_profile.for_client(),
                        "access_credentials": {"token": access_token},
                    },
                },
                status=status.HTTP_201_CREATED,
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

    except Exception as SignupTenantException:
        print("🧨 ==> user_management.signup_views.signup_as_tenant ==>", SignupTenantException)

        return Response(
            {
                STATUS_CODE: status.HTTP_500_INTERNAL_SERVER_ERROR,
                STATUS: ERROR,
                MESSAGE: SOMETHING_WENT_WRONG,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def sign_up_as_agent(request):
    try:
        serializer = SignupAgentRequestSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            first_name = serializer.validated_data.get("first_name")
            last_name = serializer.validated_data.get("last_name")
            password = serializer.validated_data.get("password")
            gender = serializer.validated_data.get("gender")

            created_user = User.objects.create_user(
                email, password, first_name=first_name, last_name=last_name
            )
            user_profile = UserProfile.objects.create(
                user=created_user, gender=gender, is_agent=True
            )

            access_token = JwtClient.encode({"email": created_user.email})

            created_user.last_login = BusinessConfig.get_current_date_time()

            created_user.save()

            return Response(
                {
                    STATUS_CODE: status.HTTP_201_CREATED,
                    STATUS: SUCCESS,
                    MESSAGE: OPERATION_SUCCESSFUL("Signup Agent User"),
                    RESULTS: {
                        **created_user.for_client(),
                        **user_profile.for_client(),
                        "access_credentials": {"token": access_token},
                    },
                },
                status=status.HTTP_201_CREATED,
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


@api_view(["POST"])
def sign_up_as_landlord(request):
    try:
        serializer = SignupLandlordRequestSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            first_name = serializer.validated_data.get("first_name")
            last_name = serializer.validated_data.get("last_name")
            password = serializer.validated_data.get("password")
            gender = serializer.validated_data.get("gender")

            created_user = User.objects.create_user(
                email, password, first_name=first_name, last_name=last_name
            )
            user_profile = UserProfile.objects.create(
                user=created_user, gender=gender, is_landlord=True
            )

            access_token = JwtClient.encode({"email": created_user.email})

            token = OtpToken.generate_otp_token()
            OtpToken.objects.create(token=token)

            created_user.last_login = BusinessConfig.get_current_date_time()

            created_user.save()

            return Response(
                {
                    STATUS_CODE: status.HTTP_201_CREATED,
                    STATUS: SUCCESS,
                    MESSAGE: OPERATION_SUCCESSFUL("Signup Landlord User"),
                    RESULTS: {
                        **created_user.for_client(),
                        **user_profile.for_client(),
                        "access_credentials": {"token": access_token},
                    },
                },
                status=status.HTTP_201_CREATED,
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
