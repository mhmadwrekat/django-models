from django.contrib import admin
from .models import Snack

# Register your models here.

@admin.register(Snack)
class AdminSnack(admin.ModelAdmin) :
    list_display = ['name', 'purchaser']
    search_fields = ['name']
    list_display_links = ('purchaser','name')
    
# Way 2
# admin.site.register(Snack)
