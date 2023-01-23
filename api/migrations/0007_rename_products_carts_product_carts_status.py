# Generated by Django 4.1.2 on 2023-01-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_orders_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carts',
            old_name='products',
            new_name='product',
        ),
        migrations.AddField(
            model_name='carts',
            name='status',
            field=models.CharField(choices=[('order-placed', 'order-placed'), ('in-cart', 'in-cart'), ('cancelled', 'cancelled')], default='in-cart', max_length=200),
        ),
    ]
