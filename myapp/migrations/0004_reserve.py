# Generated by Django 4.2.2 on 2023-07-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_image_folvika_site_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default='', max_length=20)),
                ('Lastname', models.CharField(default='', max_length=20)),
                ('Mail', models.EmailField(default='', max_length=30)),
                ('Mobile', models.IntegerField(default='')),
                ('Country', models.CharField(default='', max_length=20)),
                ('Guest', models.IntegerField(default='')),
                ('From_date', models.CharField(default='', max_length=10)),
                ('To_date', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
