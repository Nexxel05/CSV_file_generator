from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin

from schema.models import Schema, User, Column, Dataset


@admin.register(User)
class UserAdmin(BaseAdmin):
    pass


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    pass


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    pass
