# Generated by Django 4.2.2 on 2023-07-04 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_folvika_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folvika',
            old_name='image',
            new_name='site_image',
        ),
    ]