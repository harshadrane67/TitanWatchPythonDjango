# Generated by Django 3.0.5 on 2020-06-28 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_auto_20200628_1946'),
        ('Cart', '0006_auto_20200626_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.Address'),
        ),
    ]