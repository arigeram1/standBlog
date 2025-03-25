from django import forms
from article_app.models import Message,Article
from django.core.validators import ValidationError


class MessageForm(forms.ModelForm):

    class Meta:

        model = Message
        exclude = ('created_at',)
        # fields = '__all__'


    # title = forms.CharField(max_length=50)
    #
    # body = forms.CharField(widget=forms.Textarea)
    #
    # email = forms.EmailField()



