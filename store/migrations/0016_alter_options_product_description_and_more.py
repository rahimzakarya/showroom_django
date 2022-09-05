# Generated by Django 4.1 on 2022-09-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0015_delete_contacts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="options_product",
            name="description",
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name="options_product",
            name="price_unit",
            field=models.TextField(default="da/pieces", max_length=20),
        ),
        migrations.AlterField(
            model_name="products",
            name="description",
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name="products",
            name="price_unit",
            field=models.TextField(default="da/pieces", max_length=20),
        ),
    ]
