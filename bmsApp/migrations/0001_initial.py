# Generated by Django 4.2.1 on 2023-05-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("domain", models.URLField()),
                (
                    "organization_size",
                    models.CharField(
                        choices=[
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("large", "Large"),
                        ],
                        max_length=6,
                    ),
                ),
                ("expiry_date", models.DateField()),
                ("country", models.CharField(max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("verified", "Verified"),
                            ("unverified", "Unverified"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]