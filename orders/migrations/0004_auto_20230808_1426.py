# Generated by Django 3.2 on 2023-08-08 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_auto_20230807_1847'),
        ('orders', '0003_alter_orderproduct_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='vendor',
        ),
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
    ]
