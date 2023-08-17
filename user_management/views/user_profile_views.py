from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.decorators.jwt_required import jwt_required
from common.system_messages import STATUS_CODE, STATUS, SUCCESS, OPERATION_SUCCESSFUL, RESULTS, MESSAGE


@api_view(['GET'])
@jwt_required
def get_user_profile(request):
    user = request.user

    return Response({
        STATUS_CODE: status.HTTP_200_OK,
        STATUS: SUCCESS,
        MESSAGE: OPERATION_SUCCESSFUL('Fetch User Profile'),
        RESULTS: {
            'email': user.email
        }
    }, status=status.HTTP_200_OK)
