from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Info',
            {
                'fields': (
                    'user_type',
                )
            }
        )
    )


admin.site.register(NewUser, CustomUserAdmin)
