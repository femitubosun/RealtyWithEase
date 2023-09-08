from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.decorators import jwt_required, validate_request
from core.system_messages import STATUS_CODE, STATUS, MESSAGE, SUCCESS, RESULTS, OPERATION_SUCCESSFUL, OPERATION_FAIL, \
    ERROR
from user_management.serializers import ChangePasswordRequestSerializer


@api_view(["POST"])
@jwt_required
@validate_request(ChangePasswordRequestSerializer)
def change_password(request):
    try:
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        print("Old Password: ", old_password)
        print('New Password: ', new_password)

        return Response(
            {
                STATUS_CODE: status.HTTP_200_OK,
                STATUS: SUCCESS,
                MESSAGE: OPERATION_SUCCESSFUL("Change Password"),
                RESULTS: "hi",
            },
            status=status.HTTP_200_OK,
        )
    except Exception as ChangePasswordException:
        print("🧨 ==> user_management.change_password_views.change_password ==>", ChangePasswordException)

        return Response({
            STATUS_CODE: status.HTTP_500_INTERNAL_SERVER_ERROR,
            STATUS: ERROR,
            MESSAGE: OPERATION_FAIL("Change Password"),
            RESULTS: "hi",
        },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR, )
