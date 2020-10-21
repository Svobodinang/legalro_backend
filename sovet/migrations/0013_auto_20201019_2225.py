# Generated by Django 3.1.1 on 2020-10-19 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sovet', '0012_pricesection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricesection',
            options={'verbose_name': 'Секции цен', 'verbose_name_plural': 'Секции цен'},
        ),
        migrations.AlterModelOptions(
            name='servicesection',
            options={'verbose_name': 'Секции услуг', 'verbose_name_plural': 'Секции услуг'},
        ),
        migrations.CreateModel(
            name='PriceBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('priceSection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sovet.pricesection')),
            ],
            options={
                'verbose_name': 'Блоки цен',
                'verbose_name_plural': 'Блоки цен',
            },
        ),
    ]
