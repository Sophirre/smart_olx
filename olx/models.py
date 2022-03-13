from django.contrib.auth.models import AbstractUser
from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(max_length=1000, blank=True)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField()

    owner = models.ForeignKey(
        'Account',
        on_delete=models.CASCADE,
        related_name='advertisement'
    )
    # category -> One to Many


# One
class AdvertisementCategory(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(
        'Advertisement',
        # on_delete variants: CASCADE -> delete all, RESTRICT -> don't delete PROTECT -> unable to delete
        on_delete=models.CASCADE,
        related_name='category'
    )
    # subcategories -> One to Many


# Many
class AdvertisementSubCategory(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(
        'AdvertisementCategory',
        # on_delete variants: CASCADE -> delete all, RESTRICT -> don't delete PROTECT -> unable to delete
        on_delete=models.CASCADE,
        related_name='subcategory'
   )


class Account(AbstractUser):
    pass

