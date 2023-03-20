from django.contrib import admin
from .models import Post,Category,Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("topic","is_avaible")
    list_filter = ("is_avaible","date","category")
    search_fields = ("topic","date")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("topic",)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("topic",)}



