# Generated by Django 5.0.1 on 2024-01-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_auto_20210309_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='houses/photos', verbose_name='фотография'),
        ),
    ]
