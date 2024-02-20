from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)  # Changed this to EmailField to validate email addresses

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Changed fields to include email

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)  # Create a user object
        user.email = self.cleaned_data['email']  # Assign email to the user object

        if commit:
            user.save()  # Save the user object

        return user