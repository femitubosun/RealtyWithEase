from django.urls import path

from user_management.views import signup_views

urlpatterns = [
    path("signup/tenant", signup_views.sign_up_as_tenant, name="sign-up-tenant"),

]
