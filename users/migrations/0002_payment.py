# Generated by Django 5.1.4 on 2024-12-22 11:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Ims", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_date",
                    models.DateField(
                        help_text="Введите дату оплаты", verbose_name="Дата оплаты"
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Введите сумму оплаты",
                        max_digits=10,
                        verbose_name="Сумма оплаты",
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("наличная оплата", "наличная оплата"),
                            ("безналичная оплата", "безналичная оплата"),
                        ],
                        default="наличная оплата",
                        help_text="Введите метод оплаты",
                        max_length=100,
                        verbose_name="Метод оплаты",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите название оплаченного курса",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Ims.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите название оплаченного урока",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Ims.lesson",
                        verbose_name="Оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оплата",
                "verbose_name_plural": "Оплаты",
            },
        ),
    ]
