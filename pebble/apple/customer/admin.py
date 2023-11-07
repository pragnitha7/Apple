from django.contrib import admin
from .models import user_profile,Category,restaurant,Cart,foodItem
# Register your models here.
admin.site.register(user_profile)
admin.site.register(Category)
admin.site.register(restaurant)
admin.site.register(foodItem)
admin.site.register(Cart)