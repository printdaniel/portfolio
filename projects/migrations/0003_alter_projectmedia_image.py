# Generated by Django 4.2.4 on 2023-08-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_alter_projectmedia_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectmedia",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/project_images/"
            ),
        ),
    ]
