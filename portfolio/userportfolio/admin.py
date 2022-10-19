from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import AppUsers 

# Register your models here.


# Define an inline admin descriptor for AppUsers model
# which acts a bit like a singleton
class UsersInline(admin.StackedInline):
    model = AppUsers
    can_delete = False
    verbose_name_plural = 'Users'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UsersInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
