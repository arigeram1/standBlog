from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)

    father_name = models.CharField(max_length=30)

    national_code = models.CharField(max_length=10)

    image = models.ImageField(upload_to='images/profile' , blank=True , null=True)



    def __str__(self):

        return self.user.username


    class Meta:

        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'




