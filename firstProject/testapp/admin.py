from django.contrib import admin

# Register your models here.

from testapp.models import Employee,testapp_user

admin.site.register(Employee)
admin.site.register(testapp_user)