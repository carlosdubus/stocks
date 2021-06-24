# Generated by Django 3.2.4 on 2021-06-24 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=100)),
                ('series', models.CharField(max_length=10)),
                ('price_open', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_close', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_last', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_prev_close', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_low', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_high', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tottrd_qty', models.IntegerField()),
                ('tottrd_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_trades', models.IntegerField()),
                ('isin', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
