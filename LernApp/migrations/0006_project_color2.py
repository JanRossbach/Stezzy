# Generated by Django 2.0.3 on 2018-03-18 09:49

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LernApp', '0005_auto_20180318_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='color2',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]
