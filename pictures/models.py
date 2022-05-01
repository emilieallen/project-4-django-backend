from unicodedata import category
from django.db import models

# Create your models here.

CATEGORY = [
    (1, 'Night'),
    (2, 'Landscape'),
    (3, 'Urban'),
    (4, 'Architecture'),
    (5, 'Portrait'),
    (6, 'Other')
]


class Picture(models.Model):
    """
    A model for pictures.
    """

    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)

    category = models.IntegerField(
        choices=CATEGORY
        )

    location = models.CharField(max_length=10)
    picture_url = models.CharField(max_length=300)
    
    camera = models.CharField(max_length=30)
    settings = models.CharField(max_length=50)

    # saved_by = models.ManyToManyField(
    #     'jwt_auth.User',
    #     related_name='saved_pictures',
    #     blank='True'
    # )

    # added_by = models.ForeignKey(
    #     'jwt_auth.User',
    #     related_name='added_picture',
    #     on_delete=models.DO_NOTHING,
    #     blank=True
    # )

    def __str__(self):
        """Formats entries in the Admin panel"""
        return f'{self.name}'


