from django.contrib import admin
from .models import Denek
# Register your models here.

@admin.register(Denek)
class DenekAdmin(admin.ModelAdmin):
    list_filter = ('name','email')
    list_display = ('name','is_valid')
