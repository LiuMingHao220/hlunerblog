# Generated by Django 2.0.7 on 2019-05-21 23:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190521_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='评论时间'),
        ),
    ]
