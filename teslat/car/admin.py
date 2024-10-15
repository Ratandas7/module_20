from django.contrib import admin
from car.models import Brand, Model, Car, Comment, Order
# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ['brand']}
    list_display = ['brand', 'slug']

class ModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ['model']}
    list_display = ['brand', 'model', 'slug']

class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ['name']}
    list_display = ['name', 'slug', 'price', 'model', 'quantity', 'date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment', 'car', 'model', 'date']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'car_name', 'price', 'order_date']
    def car_name(self, obj):
        return obj.car.name
    def price(self, obj):
        return obj.car.price
    

admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Order, OrderAdmin)