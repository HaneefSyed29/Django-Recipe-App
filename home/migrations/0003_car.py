# Generated by Django 5.0.4 on 2024-05-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_remove_student_file_alter_student_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("car_name", models.CharField(max_length=100)),
                ("speed", models.IntegerField(default=50)),
            ],
        ),
    ]
