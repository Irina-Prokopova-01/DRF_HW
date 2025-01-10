import stripe

import config.settings
from Ims.models import Course, Lesson

stripe.api_key = config.settings.STRIPE_API_KEY


def prepare_data(prod_id, type_bd):
    """Подготовка данных для создания платежа.
    Возвращает название продукта и объект для привязки в оплате к объекту курса либо урока.
    """
    if type_bd == "course":
        return Course.objects.get(id=prod_id)
    elif type_bd == "lesson":
        return Lesson.objects.get(id=prod_id)
    else:
        raise Exception("Неверный тип базы данных")


def create_stripe_product(obj):
    """Создаем stripe продукт"""
    return stripe.Product.create(name=obj.title)



def create_stripe_price(obj, amount):
    """Создает цену в страйпе"""

    return stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product_data={"name": obj.get('name')},
    )


def create_stripe_session(price):
    """Создаёт сессию для оплаты в Stripe."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")