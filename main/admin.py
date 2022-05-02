from django.contrib import admin

from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','unikID','phone','subscription','activity')
    search_fields = ('unikID', 'name','phone','time_create',)


admin.site.register(Client,ClientAdmin)