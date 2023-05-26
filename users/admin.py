from django.contrib import admin

from users.models import User, EmailVerification
from products.admin import BasketAdmin

@admin.register(User)                                                                                   #декоратор регистрации класса
class UserAdmin(admin.ModelAdmin):

    list_display = ('username',)                                                                        #отображаемые поля в общем списке
    inline = (BasketAdmin,)                                                                              #указываем что нужно отобразить в поле юзера его корзину

#регистрация и настройка отображения emailo'в в админке
@admin.register(EmailVerification)
class EmailVerificationsAdmin(admin.ModelAdmin):

    list_display = ('code', 'user', 'expirations')
    fields = ('code', 'user', 'expirations', 'created')
    readonly_fields = ('created',)