from django.contrib import admin

from .models import Flat


class AccountAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'floor', 'has_balcony', 'active')


admin.site.register(Flat, AccountAdmin)
