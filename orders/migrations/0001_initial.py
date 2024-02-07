# Generated by Django 5.0.1 on 2024-01-25 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0004_house_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('phone', models.CharField(max_length=50, verbose_name='телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.house', verbose_name='дом')),
            ],
        ),
    ]
