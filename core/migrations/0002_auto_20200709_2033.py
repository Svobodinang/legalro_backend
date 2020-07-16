# Generated by Django 3.0.8 on 2020-07-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalinfo',
            name='garantiesTitle',
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='formText',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='formTitle',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='garantiesText',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='servicesText',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='aboutAs',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='logo',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='slogan',
            field=models.CharField(default='', max_length=30),
        ),
    ]