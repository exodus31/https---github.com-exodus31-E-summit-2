# Generated by Django 4.0.5 on 2022-08-25 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('companyname', models.CharField(default='', max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('onldesc', models.CharField(default='Not Shared Yet', max_length=1000)),
                ('qpitch', models.CharField(default='Not Shared Yet', max_length=1000)),
                ('cfunds', models.CharField(default='Not Shared Yet', max_length=1000)),
                ('rfunding', models.CharField(default='Not Shared Yet', max_length=1000)),
                ('field', models.CharField(default='General', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('details', models.CharField(default='', max_length=500)),
                ('networth', models.CharField(default='Not Shared Yet', max_length=1000)),
                ('comphold', models.CharField(default='Not Shared Yet', max_length=1000)),
                ('invfield', models.CharField(default='General', max_length=1000)),
            ],
        ),
    ]
