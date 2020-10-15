from django.contrib import admin
from .models import Product, Category

# Register your models here.


# Add fields to admin page on website.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'description',

    )

    ordering = ('sku',)

# Add fields to admin page on website.


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
