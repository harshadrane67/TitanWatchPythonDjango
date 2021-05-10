# Generated by Django 3.0.5 on 2020-06-27 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_shipping_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping_client',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.Address'),
        ),
    ]