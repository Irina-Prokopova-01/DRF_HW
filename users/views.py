from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def perform_create(self, serializer):
    #     user = serializer.save(is_active=True)
    #     user.set_password(user.password)
    #     user.save()


class UserRetrieveApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentListApiView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['payment_method']
    ordering_fields = ['date_pay']
    filterset_fields = ['lesson', 'course']