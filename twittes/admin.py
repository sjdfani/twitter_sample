from django.contrib import admin
from .models import Twittes, TwittesMedia, Like, Comment, ReTwittes


class TwittesAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    list_filter = ('user',)
    search_fields = ('user',)


class TwittesMediaAdmin(admin.ModelAdmin):
    list_display = ('twittes', 'created_at')
    list_filter = ('twittes',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'twittes', 'created_at')
    list_filter = ('user',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'twittes', 'created_at')
    list_filter = ('user',)


class ReTwittesAdmin(admin.ModelAdmin):
    list_display = ('user', 'twittes', 'created_at')
    list_filter = ('user',)


admin.site.register(Twittes, TwittesAdmin)
admin.site.register(TwittesMedia, TwittesMediaAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReTwittes, ReTwittesAdmin)
