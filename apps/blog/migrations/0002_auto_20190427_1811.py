# Generated by Django 2.0.7 on 2019-04-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='摘要'),
        ),
    ]
