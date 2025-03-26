from django.shortcuts import render,redirect

from article_app.models import Message

from .forms import MessageForm


def contactUsView(request):

    if request.method == 'POST':

        form = MessageForm(request.POST)

        if form.is_valid():

            instance = form.save(commit=False)

            instance.title += '-message'

            instance.save()

    else:

        form = MessageForm()

    return render(request,'contactus_app/contact.html' , context={'form':form})
