from django.db import models
from django.contrib.auth.models import User

from common.models import BaseModel


class UserProfile(BaseModel):
    """
    This Model defines a User's Profile Information
    """

    GENDERS = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    bvn = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDERS)
    date_of_birth = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_tenant = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    has_agreed_to_terms_and_conditions = models.BooleanField(default=False)

    def __str__(self):
        return f"<UserProfile: {User.pk}>"

    def __repr__(self):
        return f"<UserProfile: {User.pk}"
