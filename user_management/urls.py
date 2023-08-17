from django.urls import path

from user_management.views import signup_views, authentication_views, user_profile_views

urlpatterns = [
    path("signup/tenant", signup_views.sign_up_as_tenant, name="sign-up-tenant"),
    path("signup/agent", signup_views.sign_up_as_agent, name="sign-up-agent"),
    path("signup/landlord", signup_views.sign_up_as_landlord, name="sign-up-landlord"),
    path('authenticate/user', authentication_views.authenticate_user, name='authenticate-user'),
    path('user-profile', user_profile_views.get_user_profile, name='get-user-profile`')
]
