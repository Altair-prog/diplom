# Generated by Django 4.2.2 on 2024-09-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="payment_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="ID платежа"
            ),
        ),
        migrations.DeleteModel(
            name="Payment",
        ),
    ]