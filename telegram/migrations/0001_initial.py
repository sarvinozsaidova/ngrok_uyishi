# Generated by Django 5.0 on 2023-12-26 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Maxsulot nomi')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='rasmlar/', verbose_name='Rasmi')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Narhi')),
                ('column_5', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='User Id')),
                ('name', models.CharField(max_length=30, verbose_name='Ismi')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Telefon nomer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderitemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Soni')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.ordermodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.productmodel')),
            ],
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.usermodel'),
        ),
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(verbose_name='Uzunlik')),
                ('latitute', models.FloatField(verbose_name='Kenglik')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram.usermodel')),
            ],
        ),
    ]
