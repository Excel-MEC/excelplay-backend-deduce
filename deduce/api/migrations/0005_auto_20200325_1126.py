# Generated by Django 3.0.4 on 2020-03-25 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_level_is_locked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerlog',
            name='anstime',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2020, 3, 25, 11, 26, 3, 501248)),
            preserve_default=False,
        ),
    ]
