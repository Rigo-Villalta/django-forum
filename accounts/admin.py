from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ("username", "first_name", "last_name", "email", "is_active", "is_moderator", "last_login", "date_joined", )

admin.site.register(User, UserAdmin)
