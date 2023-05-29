# Generated by Django 4.1.1 on 2023-01-28 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labapp.patient')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labapp.testname')),
            ],
        ),
    ]
