from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
from django.db import models


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                "^\\w+$",
                message="Ensure this value contains only letters, numbers, and underscore.",
            ),
        ],
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=(MinValueValidator(0),),
        null=True,
        blank=True,
    )
