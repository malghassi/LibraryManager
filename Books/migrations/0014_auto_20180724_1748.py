# Generated by Django 2.0 on 2018-07-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0013_auto_20180724_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_logo',
            field=models.FileField(max_length=500, upload_to=''),
        ),
    ]
