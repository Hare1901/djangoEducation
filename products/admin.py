from django.contrib import admin
from products.views import ProductCategory, Product


admin.site.register(Product)
admin.site.register(ProductCategory)
