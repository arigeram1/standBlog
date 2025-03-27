from django.shortcuts import render,redirect

from django.contrib.auth import authenticate , login,logout

from django.contrib.auth.models import User

from .forms import LoginForm,UserEditForm

def loginView(request):

    if request.user.is_authenticated:

        return redirect('home_app:home')

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            user = User.objects.get(username=form.cleaned_data.get('username'))

            login(request,user)

            return redirect('home_app:home')

    else:

        form = LoginForm()

    return render(request, 'account_app/Login.html' , context={'form':form})


def logoutView(request):

        logout(request)

        return redirect('home_app:home')


def registerView(request):

    errors = []

    if request.user.is_authenticated:

        return redirect('home_app:home')

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
        return redirect('home_app:home')


    return render(request, 'account_app/Register.html')


def UserEditView(request):

    user = request.user

    if request.method == 'POST':
        # ایحا علت تعریف مقدار instance
        # اینه که برنامه متوجه بشه که باید داده های دریافتی از سمت فرم رو برای بروز رسانی کدوم کاربر در نظر بگیره
        # یعنی در نهایت یک فرم جدید با اطلاعات وارد شده جدید برای کاربر احراز هویت شده فعلی ساخته میشه که بعد از
        # ولیدیشن فرمش که فقط حاوی تغییراتی روی 3 فیلدش بود اعمال بشه بروی مدل user
        form = UserEditForm(instance=user,data=request.POST)

        if form.is_valid():

            form.save()


    form = UserEditForm(instance=user)

    return render(request,'account_app/edit.html' , context={'form':form})







