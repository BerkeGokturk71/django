# Generated by Django 4.1.7 on 2023-03-17 20:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text_area',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
