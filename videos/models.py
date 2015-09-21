from django.db import models


class Video(models.Model):
    NEW = 1
    RENTED = 2
    RETURNED = 3
    STATUS_CHOICES = (
        (NEW, 'New'),
        (RENTED, 'Rented'),
        (RETURNED, 'Returned'),
    )
    title = models.CharField(max_length=128)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=NEW)
