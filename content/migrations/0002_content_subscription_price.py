# Generated by Django 5.1.1 on 2024-09-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="subscription_price",
            field=models.IntegerField(
                blank=True,
                help_text="Укажите цену за подписку",
                null=True,
                verbose_name="Цена подписки",
            ),
        ),
    ]
