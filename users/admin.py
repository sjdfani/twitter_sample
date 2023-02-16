from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'username', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    list_editable = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')


admin.site.register(User, UserAdmin)
