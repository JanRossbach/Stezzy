# Generated by Django 2.0.3 on 2018-03-18 08:59

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LernApp', '0002_auto_20180317_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='color',
            field=colorfield.fields.ColorField(default='red', max_length=18),
        ),
    ]
