from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=200, required=True)
    username = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def clean(self):

        # data from the form is fetched using super function
        super(UserCreateForm, self).clean()

        # extract the username and text field from the data
        password = self.cleaned_data['password1']

        if len(password) < 5:
            self.errors['password'] = self.error_class(
                ['Minimum 5 characters required'])

        return self.cleaned_data
