# Generated by Django 4.1.7 on 2023-03-18 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_contact_text_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='text_area',
            new_name='message',
        ),
    ]
