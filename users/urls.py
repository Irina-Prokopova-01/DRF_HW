from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users.apps import UsersConfig
from rest_framework.permissions import AllowAny
from users.views import (PaymentListApiView, UserRetrieveApiView,
                         UserUpdateApiView, UserCreateAPIView)

app_name = UsersConfig.name


urlpatterns = [
    path("update/<int:pk>/", UserUpdateApiView.as_view(), name="user_update"),
    path("register/", UserCreateAPIView.as_view(), name="user_register"),
    path("retrieve/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("payment/", PaymentListApiView.as_view(), name="payment"),
    path("login/", TokenObtainPairView.as_view(permission_classes=[AllowAny]), name="login",),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=[AllowAny]), name="token_refresh",),
]