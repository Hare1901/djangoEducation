from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

from users.models import User, EmailVerification
from users.forms import UserLoginForm, UserRegistrationForm, UseProfileForm
from products.models import Basket
from common.views import TitleMixin


class UserLoginView(TitleMixin, LoginView):

    template_name = "users/login.html"
    form_class = UserLoginForm
    title = 'Авторизация'



# любой mixin всегда перед классом наследования
class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):

    model = User
    # указываем ссылку на созданый нами класс
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    # сохраняем куда перенаправит пользователя с помощью нового метода
    success_url = reverse_lazy('users:login')
    # вывод сообщения о удачном регистрации
    success_message = 'Аккаунт зарегистрирован!'
    #переменная наследуемая от моего TitleMixim
    title = 'решистрация'


class UserProfileView(TitleMixin, UpdateView):

    model = User
    form_class = UseProfileForm
    template_name = "users/profile.html"
    title = 'Личный кабинет'

    def get_success_url(self):

        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):

        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)

        return context



def logout(request):

    auth.logout(request)

    return HttpResponseRedirect(reverse('index'))


class EmailVerificationsView(TitleMixin, TemplateView):

    title = 'Подтверждение почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args,  **kwargs):

        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and email_verification.first().is_expiered():
            user.is_verifield_email = True
            user.save()

            return super(EmailVerificationsView, self).get(request, *args,  **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))

