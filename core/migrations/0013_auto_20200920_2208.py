# Generated by Django 3.1.1 on 2020-09-20 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_services_button'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benefit',
            options={'verbose_name': 'Преимущества', 'verbose_name_plural': 'Преимущества'},
        ),
        migrations.AlterModelOptions(
            name='garanty',
            options={'verbose_name': 'Гарантии', 'verbose_name_plural': 'Гарантии'},
        ),
        migrations.AlterModelOptions(
            name='generalinfo',
            options={'verbose_name': 'Основная информация', 'verbose_name_plural': 'Основная информация'},
        ),
        migrations.AlterModelOptions(
            name='runtitle',
            options={'verbose_name': 'Заголовки', 'verbose_name_plural': 'Заголовки'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услуги', 'verbose_name_plural': 'Услуги'},
        ),
    ]
