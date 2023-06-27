from django.contrib import admin
from .models import SubscribedUsers


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')


admin.site.register(SubscribedUsers, SubscribedUsersAdmin)
