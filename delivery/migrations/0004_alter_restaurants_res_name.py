# Generated by Django 5.1.6 on 2025-02-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0003_menu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurants",
            name="Res_name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
