from django import forms
from article_app.models import Message, Article
from django.core.validators import ValidationError


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('created_at',)

        # widgets = {
        #
        #     'title': forms.TextInput(
        #         attrs={
        #       'class': 'form-control',
        #       'placeholder': 'Enter Title ...',
        #       'style': ''}),
        #
        #     'body': forms.Textarea(
        #         attrs={'placeholder':'Test is text area place' , 'rows':'6'}),
        #
        #     'email': forms.EmailInput(
        #         attrs={'placeholder':'Enter Valid Email..'}
        #     )
        #
        #
        # }
