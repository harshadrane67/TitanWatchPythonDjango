# Generated by Django 3.0.5 on 2020-06-23 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0004_auto_20200623_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('town', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('pin', models.IntegerField()),
                ('state', models.CharField(max_length=120)),
                ('default', models.BooleanField(default=False)),
                ('type_add', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
