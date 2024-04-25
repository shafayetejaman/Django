from django.contrib import admin
from .models import Brand, Car

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name")}
    list_display = ["name", "slug"]


admin.site.register(CategoryAdmin)
admin.site.register(Car, Brand)
