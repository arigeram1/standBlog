from django.shortcuts import render,redirect

from article_app.models import Message

from .forms import MessageForm


def contactUsView(request):

    if request.method == 'POST':

        form = MessageForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data.get('title')
            body = form.cleaned_data.get('body')
            email = form.cleaned_data.get('email')

            Message.objects.create(title=title,body=body,email=email)

    else:

        form = MessageForm()

    return render(request,'contactus_app/contact.html' , context={'form':form})
