# Generated by Django 4.1.7 on 2023-03-15 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("schema", "0003_remove_schema_column_type_schema_columns"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dataset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dataset", models.FileField(null=True, upload_to="")),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name="schema",
            name="datasets",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="schema.dataset",
            ),
            preserve_default=False,
        ),
    ]
