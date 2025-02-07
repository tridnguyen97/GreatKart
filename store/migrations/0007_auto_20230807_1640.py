# Generated by Django 3.2 on 2023-08-07 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orderproduct_vendor'),
        ('vendors', '0001_initial'),
        ('store', '0006_auto_20230727_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vendors.vendor'),
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
