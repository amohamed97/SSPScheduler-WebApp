# Generated by Django 2.2 on 2019-09-22 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_auto_20190922_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lab',
            old_name='PeriodType',
            new_name='periodType',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='PeriodType',
            new_name='periodType',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='PeriodType',
            new_name='periodType',
        ),
    ]
