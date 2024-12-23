from django.urls import path

from users.apps import UsersConfig
from users.views import (PaymentListApiView, UserRetrieveApiView,
                         UserUpdateApiView, UserCreateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("update/<int:pk>/", UserUpdateApiView.as_view(), name="user_update"),
    path("register/", UserCreateAPIView.as_view(), name="user_register"),
    path("retrieve/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("payment/", PaymentListApiView.as_view(), name="payment"),
]