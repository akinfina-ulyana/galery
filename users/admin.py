from django.contrib import admin

from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ("email", "password")
   fields = ("email", "password")
   readonly_fields = ("email",)
   search_fields = ("email",)

