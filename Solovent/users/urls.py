from django.urls import path
from users.views import UserProfileView, UserRegistrationView, UserLoginView, EmailVerificationView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    # profile user
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    # login user
    path('login/', UserLoginView.as_view(), name='login'),
    # registration vendor
    path('registration_vendor/', UserRegistrationView.as_view(), name='registration_vendor'),
    # registration vendor
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    # logout account
    path('logout/', LogoutView.as_view(), name='logout'),
    # verification email
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),

]
