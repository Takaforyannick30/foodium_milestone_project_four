# Generated by Django 3.1.5 on 2021-02-04 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20210203_0112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='Category',
            new_name='category',
        ),
    ]