# Generated by Django 4.1.7 on 2023-03-17 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schema", "0010_rename_name_column_column_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="column",
            old_name="column_name",
            new_name="name",
        ),
    ]
