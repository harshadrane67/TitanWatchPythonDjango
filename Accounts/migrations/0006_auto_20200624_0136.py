# Generated by Django 3.0.5 on 2020-06-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='default',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='type_add',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]