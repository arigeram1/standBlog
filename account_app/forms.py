from django import forms

from django.contrib.auth.models import User

from django.core.validators import ValidationError

from django.contrib.auth import authenticate


class LoginForm(forms.Form):

    username = forms.CharField(max_length=30 , widget= forms.TextInput)

    password = forms.CharField(max_length=30 , widget= forms.PasswordInput)


    def clean(self):

        username = self.cleaned_data.get('username')

        password = self.cleaned_data.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:

            return self.cleaned_data

        else:

            raise ValidationError('username or password is incorrect', code='login_error')


    # def clean_username(self):
    #
    #     username = self.cleaned_data.get('username')
    #
    #     user = User.objects.get(username=username)
    #
    #     if user is not None:
    #
    #         raise ValidationError('this username is already exist')
    #
    #     else:
    #
    #         return self.cleaned_data.get('username')


class UserEditForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ('first_name','last_name','email')

















