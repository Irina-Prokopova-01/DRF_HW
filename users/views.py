from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from users.models import Payment, User
from rest_framework import viewsets, generics
from users.serializers import PaymentSerializer, UserSerializer, PaymentSessionRetrieveSerializer
from datetime import date
from users.services import create_stripe_price, create_stripe_product, create_stripe_session, prepare_data


class UserUpdateApiView(generics.UpdateAPIView):
    """Контроллер изменения пользователя."""
    queryset = User.objects.all()
    # serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер создания пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserRetrieveApiView(generics.RetrieveAPIView):
    """Контроллер просмотра пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyApiView(generics.DestroyAPIView):
    """Контроллер удаления пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListApiView(generics.ListAPIView):
    """Контроллер списка пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    """Реализация представления создания оплаты через generic. CreateAPIView"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        type_bd = self.request.data.get("type_bd")
        prod_id = self.request.data.get("id")
        payment_obj = prepare_data(prod_id, type_bd)
        payment = serializer.save(user=self.request.user)
        product = create_stripe_product(payment_obj.title)
        price = create_stripe_price(product, payment.amount)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()



class PaymentSessionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSessionRetrieveSerializer
    queryset = Payment.objects.all()



class PaymentListApiView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['payment_method']
    ordering_fields = ['date_pay']
    filterset_fields = ['lesson', 'course']

