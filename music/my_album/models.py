from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.


class Album(models.Model):
    CHOISES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=CHOISES,
    )

    description = models.TextField(null=True, blank=True)

    image_url = models.URLField(verbose_name="Image URL")

    price = models.FloatField(
        validators=[MinValueValidator(0.0, message="The price cannot be below 0.0")],
    )
