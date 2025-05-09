# Generated by Django 5.1.7 on 2025-03-26 04:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0007_alter_product_price_alter_product_rate"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="address",
        ),
        migrations.RemoveField(
            model_name="order",
            name="card",
        ),
        migrations.RemoveField(
            model_name="order",
            name="city",
        ),
        migrations.RemoveField(
            model_name="order",
            name="country",
        ),
        migrations.RemoveField(
            model_name="order",
            name="notes",
        ),
        migrations.RemoveField(
            model_name="order",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="order",
            name="total_price_after_discount",
        ),
        migrations.RemoveField(
            model_name="order",
            name="zip_code",
        ),
        migrations.AddField(
            model_name="order",
            name="transaction_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("paid", "Paid"),
                    ("failed", "Failed"),
                    ("cancelled", "Cancelled"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.CharField(default="pending", max_length=100)),
                ("address", models.CharField(blank=True, max_length=100, null=True)),
                ("phone", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("zip_code", models.CharField(blank=True, max_length=100, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "total_price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "total_price_after_discount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="product.card"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="product.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                through="product.OrderItem", to="product.product"
            ),
        ),
    ]
