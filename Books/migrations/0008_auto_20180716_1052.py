# Generated by Django 2.0.7 on 2018-07-16 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0007_auto_20180716_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='image_url',
            new_name='book_logo',
        ),
    ]
