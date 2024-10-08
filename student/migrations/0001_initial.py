# Generated by Django 5.0 on 2024-09-07 11:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                    "name",
                    models.CharField(
                        max_length=100,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(5)],
                    ),
                ),
                (
                    "age",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(18),
                            django.core.validators.MaxValueValidator(100),
                        ]
                    ),
                ),
                ("address", models.CharField(max_length=100)),
                ("student_id", models.IntegerField(unique=True)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
