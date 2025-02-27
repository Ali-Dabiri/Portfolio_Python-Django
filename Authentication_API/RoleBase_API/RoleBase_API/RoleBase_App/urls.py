from django.urls import path
from .views import (
    SignUpUserView, 
    LoginUserView, 
    ShowUserView, 
    CreateUserView,
    HistoryUsersView,
)
urlpatterns = [
    path('api/users/signup/', SignUpUserView.as_view(), name='user_sign_up'),
    path('api/login/', LoginUserView.as_view(), name='login'),
    path('api/users/show/', ShowUserView.as_view(), name='admin_user_show'),
    path('api/users/create/', CreateUserView.as_view(), name='admin_user_create'),
    path('api/users/history/', HistoryUsersView.as_view(), name='manager_user_history'),
]