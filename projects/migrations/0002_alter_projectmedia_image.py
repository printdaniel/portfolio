# Generated by Django 4.2.4 on 2023-08-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectmedia",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="static/project_images/"
            ),
        ),
    ]
