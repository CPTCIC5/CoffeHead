# Generated by Django 3.2.10 on 2022-10-06 10:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_music_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeimageabout',
            name='poster_image',
            field=models.ImageField(default='xyz.jpg', upload_to='Home-Poster-Images', validators=[django.core.validators.validate_image_file_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homeimageabout',
            name='image',
            field=models.ImageField(upload_to='Home-About-Image', validators=[django.core.validators.validate_image_file_extension]),
        ),
    ]
