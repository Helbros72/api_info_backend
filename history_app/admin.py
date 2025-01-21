from ipaddress import ip_address

from django.contrib import admin

from history_app.models import History


# Register your models here.
# @admin.register(History)
# class HistoryAdmin(admin.ModelAdmin):
#     list_display = ["id",]
admin.site.register(History)

