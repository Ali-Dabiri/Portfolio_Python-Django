from django.urls import path
from .views import RegisterUserView, LoginUserView, RefreshAndVerifyTokenView, AuthenticationTokenHeaderView 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [    
    path('api/users/', RegisterUserView.as_view(), name='user_registration'),
    path('api/users/authentication/', LoginUserView.as_view(), name='user_authentication'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh-and-verify/', RefreshAndVerifyTokenView.as_view(), name='refresh_and_verify_token'),
    path('api/token/authentication-token-header/', AuthenticationTokenHeaderView.as_view(), name='authentication_token_header_verify'),
]
