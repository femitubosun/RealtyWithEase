from django.forms import Form, CharField, ChoiceField, EmailField

from user_management.models.user_profile import GENDER_CHOICES


class AgentSignupForm(Form):
    

    email = EmailField(label="Email", max_length=100)
    first_name = CharField(label="First Name", max_length=100)
    last_name = CharField(label="Last Name", max_length=100)
    password = CharField(label="Password", max_length=100)
    gender = ChoiceField(label="Gender", choices=GENDER_CHOICES)

