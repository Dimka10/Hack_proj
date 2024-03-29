from django.urls import path

from .views import RegistrationView, LoginView, LogoutView, ForgotPassword, ActivateView, ForgotPasswordComplete

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('activate/<str:activation_code>/', ActivateView.as_view()),
    path('forgot_password/', ForgotPassword.as_view()),
    path('forgot_password_complete/', ForgotPasswordComplete.as_view()),
]