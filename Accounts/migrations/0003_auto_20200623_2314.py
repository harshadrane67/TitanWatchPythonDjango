# Generated by Django 3.0.5 on 2020-06-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20200623_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('0', 'Male'), ('1', 'Female'), ('2', 'Other')], default='None', max_length=10, null=True),
        ),
    ]