# Generated by Django 4.1.7 on 2023-03-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='text_area',
            field=models.CharField(max_length=500),
        ),
    ]
