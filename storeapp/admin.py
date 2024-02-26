from django.contrib import admin

from .models import User, Purchase, Product, Refund

admin.site.register(User)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Refund)
