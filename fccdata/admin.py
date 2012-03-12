from django.contrib import admin
from fccdata.models import *


class enAdmin(admin.ModelAdmin):
    list_display = ('call_sign', 'first_name', 'last_name')
    search_fields = ('call_sign',)


class amAdmin(admin.ModelAdmin):
    list_display = ('call_sign', 'operator_class', 'previous_operator_class')
    list_filter = ('operator_class', 'previous_operator_class')
    search_fields = ('call_sign',)
    raw_id_fields = ('unique_system_identifier',)


class hdAdmin(admin.ModelAdmin):
    list_display = ('call_sign', 'license_status', 'expired_date')
    list_filter = ('license_status',)
    search_fields = ('call_sign',)
    raw_id_fields = ('unique_system_identifier',)


admin.site.register(en, enAdmin)
admin.site.register(am, amAdmin)
admin.site.register(hd, hdAdmin)
