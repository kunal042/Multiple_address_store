# Generated by Django 5.0.6 on 2024-10-02 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="record",
            old_name="provinice",
            new_name="province",
        ),
    ]
