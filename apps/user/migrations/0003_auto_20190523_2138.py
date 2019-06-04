# Generated by Django 2.0.7 on 2019-05-23 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_friendship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='follower',
        ),
        migrations.DeleteModel(
            name='FriendShip',
        ),
    ]
