# Generated by Django 3.1.1 on 2020-10-19 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sovet', '0013_auto_20201019_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceblock',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('price', models.CharField(default='', max_length=100)),
                ('text', models.TextField(blank=True)),
                ('priceBlock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sovet.priceblock')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цены',
            },
        ),
    ]
