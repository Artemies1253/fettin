# Generated by Django 4.0.5 on 2022-06-26 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_lot_price_value_alter_lot_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lot',
            old_name='price_value',
            new_name='price_currency',
        ),
    ]
