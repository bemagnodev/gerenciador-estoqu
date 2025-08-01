# Generated by Django 5.0.1 on 2025-02-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_actionsstock_image_actionsstock_last_update_display_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionsstock',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor Unitário (R$)'),
        ),
        migrations.AlterField(
            model_name='cleaningproductsstock',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor Unitário (R$)'),
        ),
        migrations.AlterField(
            model_name='endomarketingstock',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor Unitário (R$)'),
        ),
    ]
