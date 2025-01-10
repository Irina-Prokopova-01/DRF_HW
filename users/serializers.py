from rest_framework.serializers import ModelSerializer, SerializerMethodField
import stripe
from users.models import Payment, User


class PaymentSessionRetrieveSerializer(ModelSerializer):
    status = SerializerMethodField()

    class Meta:
        model = User
        fields = ("status",)

    def get_status(self, obj):
        return stripe.checkout.Session.retrieve(obj.session_id,)


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"