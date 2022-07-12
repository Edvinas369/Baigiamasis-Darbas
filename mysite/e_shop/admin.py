from django.contrib import admin
from e_shop.models import Setting

# Register your models here.

class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']
    

admin.site.register(Setting,SettingtAdmin)