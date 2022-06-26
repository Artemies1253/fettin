# Generated by Django 4.0.5 on 2022-06-26 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_currencyuser_currency_alter_currencyuser_user'),
        ('exchange', '0002_remove_lot_value_lot_price_lot_selled_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='price_value',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='currency.currency', verbose_name='Вид ценовой валюты'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lot',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lots', to='currency.currency', verbose_name='Вид продаваемой валюты'),
        ),
    ]
