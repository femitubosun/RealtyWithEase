import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('This object requires an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user

    def get_tenants(self):
        self.filter(is_tenant=True)


class User(AbstractBaseUser, PermissionsMixin):
    """
    This defines the custom User model for the project
    """
    email = models.EmailField(max_length=255, unique=True)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @staticmethod
    def create_user(email: str, password: str, **extra_fields) -> "User":
        """
        Create a user
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
