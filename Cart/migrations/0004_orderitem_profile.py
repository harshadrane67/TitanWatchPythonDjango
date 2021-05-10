# Generated by Django 3.0.5 on 2020-06-26 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_auto_20200624_0136'),
        ('Cart', '0003_auto_20200626_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.Profile'),
        ),
    ]
