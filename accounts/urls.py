from django.urls import path
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    UserRegisterView, UserRegisterVerifyCodeView,
    UserLoginView, UserLogoutView,
    ProfileUpdateView, ProfileDetailView
)

app_name = 'accounts'

urlpatterns = [
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('verify/', UserRegisterVerifyCodeView.as_view(), name='verify_code'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
]
