from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInline(admin.StackedInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'id')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'floor', 'has_balcony', 'active')
    raw_id_fields = ('liked_by',)
    inlines = [OwnersInline]


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
    list_display = ('name', 'pure_phonenumber', 'owned_flats')
    raw_id_fields = ('flats',)

    def owned_flats(self, obj):
        return ', '.join(str(flat.id) for flat in obj.flats.all())


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
