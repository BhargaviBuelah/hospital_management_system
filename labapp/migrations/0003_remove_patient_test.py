# Generated by Django 4.1.1 on 2023-01-29 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0002_tests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='test',
        ),
    ]
