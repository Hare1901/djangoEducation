from django.contrib import admin
from products.views import ProductCategory, Product, Basket
admin.site.register(ProductCategory)

@admin.register(Product)                                                                                #Регистарция модели с настройками
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')                                                #указываем какие поля из модели отобьражать в админке
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')                              # что отображать в конкретном Product(каждый кортеж - отображение на одной строке) порядок важен
    search_fields = ('name',)                                                                       #поле для поиска, указывыается поле по которому будет идти поиск
    ordering = ('name', )                                                                           #настройка отображения не по id в бд( если необходимо


class BasketAdmin(admin.TabularInline):                                                                #указание что эта модель - часть другой модели(необходим вторичный ключ(ForeignKey))
    model = Basket
    fields = ('products', 'quantity',)
    extra = 0                                                                                       #количество дополнительных полей для добавления товара через админку