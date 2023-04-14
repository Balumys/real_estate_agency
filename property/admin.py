from django.contrib import admin

from .models import Flat


class AccountAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']


admin.site.register(Flat, AccountAdmin)
