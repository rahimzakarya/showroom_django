# Generated by Django 4.1 on 2022-08-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_product_image_alter_product_price_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]