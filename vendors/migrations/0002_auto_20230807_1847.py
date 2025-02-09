# Generated by Django 3.2 on 2023-08-07 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='username',
        ),
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
