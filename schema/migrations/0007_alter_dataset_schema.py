# Generated by Django 4.1.7 on 2023-03-16 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("schema", "0006_remove_schema_datasets_dataset_schema"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="schema",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="datasets",
                to="schema.schema",
            ),
        ),
    ]
