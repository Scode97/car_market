# Generated by Django 2.0.6 on 2018-07-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20180715_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_img',
            field=models.ImageField(upload_to=''),
        ),
    ]
