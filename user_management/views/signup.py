from django.shortcuts import render

from user_management.forms import TenantSignupForm


def sign_up_as_tenant(request):
    form = TenantSignupForm()

    return render(request, 'user_management/signup/tenant_signup.html', {"form": form})
