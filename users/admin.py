from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


class UserAdmin(UserAdmin):
    list_display = (
        'email', 'username', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    list_editable = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    ordering = ('email',)
    fieldsets = (
        (_('Personal information'), {
            'fields': ('email', 'username', 'fullname', 'bio', 'locations', 'website', 'birthdate', 'cover_photo', 'profile_photo', 'password')
        }),
        (_('Date information'), {
            'fields': ('date_joined', 'last_login')
        }),
        (_('Other information'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'fullname', 'bio', 'locations', 'website', 'birthdate', 'cover_photo', 'profile_photo'
            )
        }),
    )


admin.site.register(User, UserAdmin)
