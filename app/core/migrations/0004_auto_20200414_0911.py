# Generated by Django 3.0.5 on 2020-04-14 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ingridient'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingridient',
            new_name='Ingredient',
        ),
    ]
