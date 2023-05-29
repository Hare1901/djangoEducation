from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
    is_verifield_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expirations = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    # формирование и отправка ссылки для пордтверждения email'а
    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={
            'email': self.user.email,
            'code': self.code
        })
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учетной записи для {self.user.username}'
        message = 'для подтверждения учетной записи перейдите {} перейдите по ссылку {}'.format(
            self.user.email,
            verification_link,
        )
        send_mail(
            subject=subject,
            message=message,
            # вместо очевидного эиэйла указываем переменную из settings
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False
        )

    def is_expirations(self):

        return True if now() <= self.expirations else False
