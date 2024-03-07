from django.urls import path
from .views import (
    RegisterView, 
    VerifyEmail, 
    LoginAPIView, 
    PasswordTokenCheck, 
    RequestPasswordReset,
    SetNewPassword
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('request-password-reset/', RequestPasswordReset.as_view(), name='request-password-reset'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheck.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPassword.as_view(), name='password-reset-complete')
    
]

 
