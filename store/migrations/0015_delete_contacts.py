# Generated by Django 4.1 on 2022-09-02 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0014_rename_contact_contacts"),
    ]

    operations = [
        migrations.DeleteModel(name="contacts",),
    ]