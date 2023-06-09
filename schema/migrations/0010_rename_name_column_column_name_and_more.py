# Generated by Django 4.1.7 on 2023-03-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schema", "0009_remove_column_first_name_remove_column_last_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="column",
            old_name="name",
            new_name="column_name",
        ),
        migrations.RemoveField(
            model_name="column",
            name="age_max_value",
        ),
        migrations.RemoveField(
            model_name="column",
            name="age_min_value",
        ),
        migrations.AlterField(
            model_name="column",
            name="type",
            field=models.CharField(
                choices=[
                    ("Full name", "Name"),
                    ("Job", "Job"),
                    ("Email", "Email"),
                    ("Company", "Company"),
                    ("Date", "Date"),
                ],
                max_length=100,
            ),
        ),
    ]
