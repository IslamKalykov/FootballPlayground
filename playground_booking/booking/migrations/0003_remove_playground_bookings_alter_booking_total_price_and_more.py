# Generated by Django 5.0.1 on 2024-01-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("booking", "0002_remove_customuser_id_playground_playground_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playground",
            name="bookings",
        ),
        migrations.AlterField(
            model_name="booking",
            name="total_price",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_permissions",
            field=models.ManyToManyField(
                related_name="custom_user_groups", to="auth.permission"
            ),
        ),
    ]