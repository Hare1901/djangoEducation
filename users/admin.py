from django.contrib import admin

from users.models import User
from products.admin import BasketAdmin

@admin.register(User)                                                                                   #декоратор регистрации класса
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)                                                                        #отображаемые поля в общем списке
    inline = (BasketAdmin,)                                                                              #указываем что нужно отобразить в поле юзера его корзину
    