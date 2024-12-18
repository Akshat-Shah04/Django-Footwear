from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("pname", "brand", "price", "seller")

    # Override to filter only users with the seller role
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "seller":
            # Filter users to show only those with the role of "seller"
            kwargs["queryset"] = User.objects.filter(role="seller")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class WishListAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "ttime")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            # Filter users to show only those with the role of "buyer"
            kwargs["queryset"] = User.objects.filter(role="buyer")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "payment", "time_date", "roundtotal")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            # Filter users to show only those with the buyer role
            kwargs["queryset"] = User.objects.filter(role="buyer")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Wishlist, WishListAdmin)
admin.site.register(Coupon)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
admin.site.register(Billing)
admin.site.register(Order)
