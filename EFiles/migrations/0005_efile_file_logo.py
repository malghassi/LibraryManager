# Generated by Django 2.0 on 2018-07-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EFiles', '0004_remove_efile_book_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='efile',
            name='file_logo',
            field=models.FileField(default='', max_length=500, upload_to=''),
        ),
    ]
