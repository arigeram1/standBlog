from django.shortcuts import render,redirect

from django.contrib.auth import authenticate , login,logout

from django.contrib.auth.models import User

def loginView(request):

    if request.user.is_authenticated:

        return redirect('/')

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            return redirect('/login')

    return render(request, 'account_app/Login.html')


def logoutView(request):

        logout(request)

        return redirect('/')



def registerView(request):

    errors = []

    if request.user.is_authenticated:

        return redirect('/')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:

            errors.append('passwords are not same')
            return render(request, 'account_app/Register.html', context={'errors':errors})

        user = User.objects.create(username=username,password=password1,email=email)

        login(request,user)
        return redirect('/')


    return render(request, 'account_app/Register.html')









