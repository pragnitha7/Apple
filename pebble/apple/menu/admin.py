from django.contrib import admin
from .models import foodItem,Category


class foodItemAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('food_name',)}
    search_fields=('food_name','category__category_name','vendor__vendor_name','price')
    list_filter=('is_available',)
    list_display=('food_name','vendor','price','is_available','updated_at')

admin.site.register(foodItem,foodItemAdmin)
