# Generated by Django 3.2.8 on 2021-11-29 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_photos_phone_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='photos',
            new_name='Images',
        ),
    ]