# Generated by Django 5.1.6 on 2025-03-06 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0009_alter_author_is_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='user',
            new_name='name',
        ),
    ]
