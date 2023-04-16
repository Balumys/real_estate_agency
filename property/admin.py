from django.contrib import admin

from .models import Flat, Complaint, Owner


class AccountAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'floor', 'has_balcony', 'active')
    raw_id_fields = ('liked_by',)


class ComplainAdmin(admin.ModelAdmin):
    search_fields = ('flat_complaint', 'user')
    raw_id_fields = ('flat_complaint', 'user')
    list_display = ('flat_complaint', 'user', 'complaint_preview')

    def complaint_preview(self, obj):
        if len(obj.complaint_text) > 50:
            return obj.complaint_text[:50] + '...'
        else:
            return obj.complaint_text


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'pure_phonenumber')
    raw_id_fields = ('flats',)


admin.site.register(Flat, AccountAdmin)
admin.site.register(Complaint, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
