# Generated by Django 2.2 on 2019-05-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_group_lecplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='lecType',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]