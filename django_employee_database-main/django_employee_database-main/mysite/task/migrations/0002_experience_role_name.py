# Generated by Django 4.2.5 on 2024-02-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="role_name",
            field=models.CharField(default="null", max_length=100),
        ),
    ]
