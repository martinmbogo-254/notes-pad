# Generated by Django 3.2.9 on 2021-11-22 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_note_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='description',
            new_name='note',
        ),
    ]
