# Generated by Django 2.0.4 on 2018-04-30 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_viaje_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
