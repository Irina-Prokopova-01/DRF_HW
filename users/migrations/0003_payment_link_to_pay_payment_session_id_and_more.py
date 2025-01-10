# Generated by Django 5.1.4 on 2025-01-04 09:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="link_to_pay",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="ID сессии"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Введите сумму оплаты",
                max_digits=10,
                null=True,
                verbose_name="Сумма оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_date",
            field=models.DateField(
                blank=True,
                help_text="Введите дату оплаты",
                null=True,
                verbose_name="Дата оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
