from django.contrib import admin

from .models import Flat, Complaint


class AccountAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'floor', 'has_balcony', 'active')


class ComplainAdmin(admin.ModelAdmin):
    search_fields = ('flat_complaint', 'user')
    raw_id_fields = ('flat_complaint', 'user')
    list_display = ('flat_complaint', 'user', 'complaint_preview')

    def complaint_preview(self, obj):
        if len(obj.complaint_text) > 50:
            return obj.complaint_text[:50] + '...'
        else:
            return obj.complaint_text


admin.site.register(Flat, AccountAdmin)
admin.site.register(Complaint, ComplainAdmin)
