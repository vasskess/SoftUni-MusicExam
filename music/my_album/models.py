from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30

    ARTIST_MAX_LEN = 30

    GENRE_MAX_LEN = 30

    MIN_PRICE_VALUE = 0.0

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_NUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIPHOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    CHOICES = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_NUSIC, RNB_NUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIPHOP_MUSIC, HIPHOP_MUSIC),
        (OTHER, OTHER),
    )

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
        verbose_name="Album Name"
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=CHOICES,
    )

    description = models.TextField(null=True, blank=True)

    image_url = models.URLField(verbose_name="Image URL")

    price = models.FloatField(
        validators=[MinValueValidator(MIN_PRICE_VALUE, message=f"The price cannot be below {MIN_PRICE_VALUE}")],
    )
