# Generated by Django 4.0.5 on 2022-08-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testx', '0013_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
