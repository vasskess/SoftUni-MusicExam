# Generated by Django 4.1.2 on 2022-10-24 17:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_album", "0004_alter_album_album_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="price",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        0.0, message="The price cannot be below 0.0"
                    )
                ]
            ),
        ),
    ]
