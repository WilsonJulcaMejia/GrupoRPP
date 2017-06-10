from django.contrib import admin

# Register your models here.
from news.models import New


class NewAdmin(admin.ModelAdmin):
    model = New
    list_display = ['id', 'title', 'created_at', 'is_enabled']


admin.site.register(New, NewAdmin)
