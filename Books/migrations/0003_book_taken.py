# Generated by Django 2.0.7 on 2018-07-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_delete_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='taken',
            field=models.BooleanField(default=False),
        ),
    ]