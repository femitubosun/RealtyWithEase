import uuid

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):

    def create_tenant_user(self, email, password: str, **extra_fields):
        """
        Create and save a user with email and password
        :param email: User unique Email
        :param password: User plain Password
        :param extra_fields: Other fields
        :return: User
        """

        if not email or not password:
            raise ValueError('Email and Password must be set')
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save()

        return user


class User(AbstractUser):
    """
    This defines the custom User model for the project
    """
    username = models.CharField(max_length=20, default=None, blank=True, null=True, unique=True)  # type: ignore
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=True)
    has_verified_email = models.BooleanField(default=False)

    @staticmethod
    def create_tenant_user(email: str, password: str, **extra_fields) -> "User":
        """
        Create a tenant user
        :param email: User unique Email
        :param password: User plain Password
        :param extra_fields: Other fields
        :return:
        """

        if not email or not password:
            raise ValueError('Email and Password must be set')
        user = User(email=email, password=make_password(password))

        user.save()
        return user

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
