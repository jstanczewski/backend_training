# Generated by Django 3.0.10 on 2021-04-27 18:38

import django.core.validators
from django.db import migrations, models
import viewer.models


class Migration(migrations.Migration):

    dependencies = [
        ("viewer", "0002_movie"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=viewer.models.get_upload_path,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=[
                            "bmp",
                            "jpg",
                            "jpeg",
                            "jpe",
                            "gif",
                            "tif",
                            "tiff",
                            "png",
                        ]
                    )
                ],
            ),
        ),
    ]
