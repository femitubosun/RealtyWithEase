from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.infrastructure.internal import JwtClient
from config import BusinessConfig
from user_management.forms import AgentSignupForm, LandlordSignupForm
from user_management.models import User, UserProfile
from user_management.serializers import SignupTenantRequestSerializer
from common.system_messages import STATUS_CODE, STATUS, ERROR, MESSAGE, RESULTS, VALIDATION_ERROR, SUCCESS, \
    OPERATION_SUCCESSFUL, SOMETHING_WENT_WRONG


@api_view(['POST'])
def sign_up_as_tenant(request):
    try:
        serializer = SignupTenantRequestSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            password = serializer.validated_data.get('password')
            gender = serializer.validated_data.get('gender')

            created_user = User.objects.create_user(email, password, first_name=first_name, last_name=last_name)
            user_profile = UserProfile.objects.create(user=created_user, gender=gender, is_tenant=True)

            access_token = JwtClient.encode({
                'email': created_user.email
            })

            created_user.last_login = BusinessConfig.get_current_date_time()

            return Response({
                STATUS_CODE: status.HTTP_201_CREATED,
                STATUS: SUCCESS,
                MESSAGE: OPERATION_SUCCESSFUL('Signup Tenant User'),
                RESULTS: {
                    'user': {
                        **created_user.for_client(),
                        'profile': user_profile.for_client()
                    },
                    'access_credentials': {
                        'token': access_token
                    }
                }
            }, status=status.HTTP_201_CREATED)

        return Response({
            STATUS_CODE: status.HTTP_400_BAD_REQUEST,
            STATUS: ERROR,
            MESSAGE: VALIDATION_ERROR,
            RESULTS: serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print("🧨-> user_management.authenticate_user_error:", e)

        return Response({
            STATUS_CODE: status.HTTP_500_INTERNAL_SERVER_ERROR,
            STATUS: ERROR,
            MESSAGE: SOMETHING_WENT_WRONG,
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def sign_up_as_agent(request):
    form = AgentSignupForm()

    if request.method == 'POST':

        filled_agent_signup_form = AgentSignupForm(request.POST)

        if filled_agent_signup_form.is_valid():
            email = filled_agent_signup_form.cleaned_data['email']
            first_name = filled_agent_signup_form.cleaned_data['first_name']
            last_name = filled_agent_signup_form.cleaned_data['last_name']
            password = filled_agent_signup_form.cleaned_data['password']
            gender = filled_agent_signup_form.cleaned_data['gender']

            created_user = User.create_user(email, password, first_name=first_name, last_name=last_name)
            UserProfile.objects.create(user=created_user, gender=gender, is_agent=True)

            return render(request, "user_management/signup/agent_signup.html", {"form": form})

        else:
            return render(request, "user_management/signup/agent_signup.html", {"form": filled_agent_signup_form})

    return render(request, 'user_management/signup/agent_signup.html', {"form": form})


def sign_up_as_landlord(request):
    # Create instance of empty LandlordSignupForm
    form = LandlordSignupForm()

    # Handle POST request
    if request.method == 'POST':
        # Create instance of LandlordSignupForm with data in a request.POST
        filled_landlord_signup_form = LandlordSignupForm(request.POST)

        if filled_landlord_signup_form.is_valid():
            email = filled_landlord_signup_form.cleaned_data['email']
            first_name = filled_landlord_signup_form.cleaned_data['first_name']
            last_name = filled_landlord_signup_form.cleaned_data['last_name']
            password = filled_landlord_signup_form.cleaned_data['password']
            gender = filled_landlord_signup_form.cleaned_data['gender']

            created_user = User.create_user(email, password, first_name=first_name, last_name=last_name)
            UserProfile.objects.create(user=created_user, gender=gender, is_landlord=True)

            return render(request, "user_management/signup/landlord_signup.html", {"form": form})
        else:

            return render(request, "user_management/signup/landlord_signup.html", {"form": filled_landlord_signup_form})

    return render(request, 'user_management/signup/landlord_signup.html', {"form": form})
