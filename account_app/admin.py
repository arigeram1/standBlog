from django.contrib import admin

from .models import Profile

from standBlog import settings

admin.site.register(Profile)


# if settings.LANGUAGE_CODE == 'fa-ir':
#     admin.site.site_header = 'پنل مدیریت'
