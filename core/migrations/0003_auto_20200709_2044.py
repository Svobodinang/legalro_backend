# Generated by Django 3.0.8 on 2020-07-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200709_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='servicesText',
            field=models.CharField(default='', max_length=500),
        ),
    ]
