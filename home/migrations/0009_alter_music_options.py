# Generated by Django 3.2.10 on 2022-10-07 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20221007_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['uploaded_on']},
        ),
    ]
