from django.shortcuts import render

def login(request):

    return render(request,'account_app/Login.html')