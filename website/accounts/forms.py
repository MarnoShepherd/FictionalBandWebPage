from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    """
    Custom user registration form based on Django's UserCreationForm.

    This form extends the UserCreationForm to include additional attributes
    and styling for the registration fields.

    Attributes:
        username (CharField): The field for the username.
        email (EmailField): The field for the user's email address.
        password1 (CharField): The field for the user's password (first input).
        password2 (CharField): The field for confirming the user's password (second input).

    Meta:
        model (User): The User model to be used for registration.
        fields (list): The fields to be included in the form, including
            'username', 'email', 'password1', and 'password2'.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the SignupForm.

        This constructor sets attributes and placeholders for the form fields
        to customize their appearance in the registration form.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        # Customize field attributes and placeholders
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    