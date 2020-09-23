from django.contrib import admin
from .models import Userorders, SingleOrder

# Register your models here.

class OrderSingleItemAdministration(admin.TabularInline):
    model = SingleOrder
    readonly_fields = ('singleordertotal',)

class OrderAdministration(admin.ModelAdmin):

    inlines = (OrderSingleItemAdministration,)

    readonly_fields = ('orderid', 'orderdate', 'delivery', 'total', 'finaltotal',)

    fields = ('orderid', 'firstname', 'lastname', 'emailaddress',
                'phone', 'address1', 'address2', 'town', 'county',
                'postalcode', 'country', 'orderdate', 'delivery',
                'total', 'finaltotal',)
            
    order_display = ('orderid', 'orderdate', 'firstname', 'lastname', 'total', 'delivery', 'finaltotal',)

    ordering = ('-orderdate',)

admin.site.register(Userorders, OrderAdministration)
    