# Generated by Django 3.0.5 on 2020-06-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='product_img')),
                ('model', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=120)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('discount', models.IntegerField(blank=True)),
                ('offer_val', models.IntegerField(blank=True)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
