# Generated by Django 4.1.7 on 2023-03-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denek', '0002_denek_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='denek',
            name='is_valid',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
