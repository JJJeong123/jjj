# Generated by Django 4.0.1 on 2022-02-16 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_remove_shop_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.member', verbose_name='manager'),
        ),
    ]
