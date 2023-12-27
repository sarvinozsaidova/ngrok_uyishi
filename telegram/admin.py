from django.contrib import admin
from .models import User, Product, Order, Orderitem, Location

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(Location)
