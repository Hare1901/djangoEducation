from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import UserLoginView, UserRegistrationView, UserProfileView, EmailVerificationsView

app_name = "users"
urlpatterns = [
    path('users/login/', UserLoginView.as_view(), name="login"),
    path('registration/', UserRegistrationView.as_view(), name="registration"),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name="profile"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('verify/<str:email>/<uuid:code>', EmailVerificationsView.as_view(), name="email_verification"),

]

