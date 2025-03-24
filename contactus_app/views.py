from django.shortcuts import render,redirect

from .forms import ContactUsForm


def contactUsView(request):

    if request.method == 'POST':

        form = ContactUsForm(data=request.POST)

        if form.is_valid():

            print(form.cleaned_data['name'])

    else:

        form = ContactUsForm()


    return render(request,'contactus_app/contact.html' , context={'form':form})
