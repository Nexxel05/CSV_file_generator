from django.conf import settings
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
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=100,
        choices=ColumnTypes.choices
    )
    order = models.PositiveSmallIntegerField()
    age_min_value = models.PositiveSmallIntegerField(blank=True, null=True)
    age_max_value = models.PositiveSmallIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Schema(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    columns = models.ManyToManyField(
        Column,
        related_name="schemas"
    )
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Dataset(models.Model):
    dataset = models.FileField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    schema = models.ForeignKey(
        Schema,
        on_delete=models.CASCADE,
        related_name="datasets"
    )
