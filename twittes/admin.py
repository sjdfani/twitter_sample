from django.contrib import admin
from .models import Twittes


class TwittesAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    list_filter = ('user',)
    search_fields = ('user',)


admin.site.register(Twittes, TwittesAdmin)
