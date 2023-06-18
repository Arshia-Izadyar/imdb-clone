# Generated by Django 3.2 on 2023-06-12 15:01

from django.db import migrations, models
import lib.validator


class Migration(migrations.Migration):
    dependencies = [
        ("Movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewmodel",
            name="rating",
            field=models.DecimalField(decimal_places=1, max_digits=4, validators=[lib.validator.check_rate]),
        ),
    ]
