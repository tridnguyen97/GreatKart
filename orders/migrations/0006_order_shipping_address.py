# Generated by Django 3.2 on 2023-08-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20230809_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(default='1 Hoang Van Thu, quan 5, TPHCM', max_length=100),
            preserve_default=False,
        ),
    ]
