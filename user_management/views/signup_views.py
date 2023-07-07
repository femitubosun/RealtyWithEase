from django.shortcuts import render

from user_management.forms import * #TenantSignupForm, AgentSignupForm
from user_management.models import User, UserProfile


def sign_up_as_tenant(request):
    """
    This method handles request to signup up a tenant
    :param request:
    :return:
    """

    # Create instance of empty TenantSignupForm
    form = TenantSignupForm()

    # Handle POST request
    if request.method == 'POST':
        # Create instance of TenantSignupFrom with data in request.POST
        filled_signup_form = TenantSignupForm(request.POST)

        # If the form is valid create tenant user else render the filled form
        if filled_signup_form.is_valid():
            email = filled_signup_form.cleaned_data['email']
            first_name = filled_signup_form.cleaned_data['first_name']
            last_name = filled_signup_form.cleaned_data['last_name']
            password = filled_signup_form.cleaned_data['password']
            gender = filled_signup_form.cleaned_data['gender']

            created_user = User.create_user(email, password, first_name=first_name, last_name=last_name)
            UserProfile.objects.create(user=created_user, gender=gender, is_tenant=True)

            return render(request, "user_management/signup/tenant_signup.html", {"form": form})

        else:
            return render(request, "user_management/signup/tenant_signup.html", {"form": filled_signup_form})

    return render(request, 'user_management/signup/tenant_signup.html', {"form": form})



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

