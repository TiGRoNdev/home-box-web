# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0004_auto_20170826_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
