from django.contrib import admin

from .models import Category, Product, Tag, Order, Cart

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','date','price')

class CartAdmin(admin.ModelAdmin):
    list_display = ('user','user')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
