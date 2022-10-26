from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from project.forms import RegistrationForm
from project.models import *


admin.site.register(project)
admin.site.register(projectCategory)
admin.site.register(Reply)
admin.site.register(Category)

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        })
    )
    add_form = RegistrationForm()