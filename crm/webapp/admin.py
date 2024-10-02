from django.contrib import admin
from .models import Record

# Register your models here.

# admin.site.register(Record)
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    

