# Generated by Django 2.2 on 2019-05-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_group_groupnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='lecInstName',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]