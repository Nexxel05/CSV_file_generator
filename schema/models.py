from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Column(models.Model):
    class ColumnTypes(models.TextChoices):
        NAME = "Full name"
        AGE = "Age"
        EMAIL = "Email"
        COMPANY = "Company"
        DATE = "Date"
    name = models.CharField(max_length=63)
    type = models.CharField(
        max_length=100,
        choices=ColumnTypes.choices
    )
    order = models.PositiveSmallIntegerField()
    age_min_value = models.PositiveSmallIntegerField(blank=True, null=True)
    age_max_value = models.PositiveSmallIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
