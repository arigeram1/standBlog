from django import forms

# در اینجا با کمک کلاس زیر یک فرم با اینپوت های مختلف درست میکنیم

# که بعد یک نمونه از روی این کلاس باید ساخته شود که فرم نهایی ما است و در ویو به صفحه مورد نظر

# ارسال شود با کمک کانتکس

class ContactUsForm(forms.Form):

    name = forms.CharField(max_length=10 , label='Name :')
    text = forms.CharField(max_length=10 , label='Text :')


