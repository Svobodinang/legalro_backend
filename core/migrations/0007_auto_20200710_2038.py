# Generated by Django 3.0.8 on 2020-07-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_runtitle_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garanty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='runtitle',
            name='key',
        ),
    ]