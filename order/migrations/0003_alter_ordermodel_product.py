# Generated by Django 4.2.3 on 2023-09-20 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_addproductmodel_status'),
        ('order', '0002_remove_ordermodel_is_order_ordermodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.addproductmodel'),
        ),
    ]
