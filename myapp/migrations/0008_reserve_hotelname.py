# Generated by Django 4.2.2 on 2023-07-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_reserv_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='hotelname',
            field=models.CharField(default='', max_length=35),
        ),
    ]